import threading
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Any, Callable, Dict, Optional
from enum import Enum

from shared_kernel.config import Config
from shared_kernel.interfaces import DataBus
from shared_kernel.logger import Logger
from shared_kernel.messaging.utils.event_messages import AWSReceiveEventMessage
from shared_kernel.status_tracker import StatusTracker

app_config = Config()
logger = Logger(app_config.get("APP_NAME"))


class TaskStatus(Enum):
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"


class EventExecutor:
    def __init__(self, databus: DataBus, status_tracker: StatusTracker):
        """
        Initialize the event executor.
        
        Args:
            databus: databus - AWS Databus (SQS and Events) / NATS / HTTP
            status_tracker: Status tracker to track status of events task and jobs
        """
        self.databus = databus
        self.status_tracker = status_tracker
        # listener threads for each events
        self._threads: Dict[str, threading.Thread] = {}
        # concurrent executors for each event
        self._executors: Dict[str, ThreadPoolExecutor] = {}
        self._shutdown_event = threading.Event()
        self._active_futures: Dict[str, set[Future]] = {}

    def _process_message(
        self,
        event_msg: AWSReceiveEventMessage,
        callback: Callable[[dict, Optional[dict]], None],
    ) -> bool:
        """
        Process a single message with error handling
        
        Args:
            event_msg: Parsed event message
            callback: Handler function to process the message
            
        Returns:
            bool: True if processing succeeded, False otherwise
        """
        try:
            task: dict = self.status_tracker.get_task(task=event_msg.event_name, task_id=event_msg.job_id)
            
            if task is None:
                self.status_tracker.create_task(
                    trace_id=event_msg.trace_id,
                    span_id=event_msg.span_id, 
                    task=event_msg.event_name,
                    status=TaskStatus.PROCESSING.value,
                    task_id=event_msg.job_id
                )

                # NOTE: From where are we going to set the tracking payload for an event

                self.status_tracker.set_tracking_payload(
                    span_id=event_msg.span_id,
                    trace_id=event_msg.trace_id, 
                    task=event_msg.event_name,
                    tracking_payload=event_msg.payload,
                    task_id=event_msg.job_id
                )

                callback(event_msg.payload, None)
                
            elif task["status"] == TaskStatus.PROCESSING.value:
                callback(event_msg.payload, task.get("tracking_payload"))
                
            return True

        except Exception as e:
            logger.error(
                f"Error processing event {event_msg.event_name}: {str(e)}"
            )
                
            self.status_tracker.mark_task_as_failure(
                span_id=event_msg.span_id,
                trace_id=event_msg.trace_id,
                task=event_msg.event_name,
                failure_reason=str(e),
                task_id=event_msg.job_id
            )

            # NOTE: dead letter queue is yet to be implemented

            # self.databus.sent_to_dead_letter_queue(
            #     event_msg.event_name,
            #     event_msg.__dict__,
            #     e
            # )

            return False

    def _callback_wrapper(
        self,
        callback: Callable[[Any], None],
        message: dict
    ) -> None:
        """
        Wrapper around message processing to handle cleanup and status updates.
        """
        success = False
        
        try:
            event_msg = AWSReceiveEventMessage(message)
            success = self._process_message(event_msg, callback)
        finally:
            if success:
                self.status_tracker.update_task(
                    span_id=event_msg.span_id,
                    trace_id=event_msg.trace_id,
                    task=event_msg.event_name,
                    status=TaskStatus.COMPLETED.value,
                    task_id=event_msg.job_id
                )
            self.databus.delete_message(event_msg)

    def _listen_events(
        self,
        event_name: str,
        executor: ThreadPoolExecutor,
        callback: Callable[[Any], None],
    ) -> None:
        """
        Main event listening loop for a specific event type.
        """
        while not self._shutdown_event.is_set():
            try:
                message = self.databus.get_async_message(event_name)
                if message:
                    future = executor.submit(
                        self._callback_wrapper,
                        callback,
                        message
                    )
                    self._active_futures[event_name].add(future)
            except Exception as e:
                logger.error(f"Error in event listener for {event_name}: {str(e)}")

    def register_event(
        self,
        event_name: str,
        callback: Callable[[Any], None],
        max_concurrency: int,
    ) -> None:
        """
        Register an event handler with the specified concurrency limit.

        Args:
            event_name: Name of the event to handle
            callback: Function to call with the event payload
            max_concurrency: Maximum number of concurrent executions
            
        Raises:
            ValueError: If event is already registered
        """
        if event_name in self._threads:
            raise ValueError(f"Event {event_name} is already registered")

        # the DataBus interface requires subscribe_async_event
        # to accept a callback parameter as part of its method signature.
        self.databus.subscribe_async_event(event_name, None)

        executor = ThreadPoolExecutor(
            max_workers=max_concurrency,
            thread_name_prefix=f"Executor-{event_name}"
        )
        self._executors[event_name] = executor

        # keeping track of active futures returned by
        # submitting a job to the threadpool executor
        self._active_futures[event_name] = set()

        thread = threading.Thread(
            target=self._listen_events,
            args=(event_name, executor, callback),
            name=f"EventListener-{event_name}",
            daemon=True
        )
        self._threads[event_name] = thread
        thread.start()

    def shutdown(self) -> None:
        """
        Gracefully shut down all event listeners.
        """
        self._shutdown_event.set()

        # wait for threads to finish
        for event_name, thread in self._threads.items():
            thread.join()

        # wait for active tasks to complete
        for event_name, futures in self._active_futures.items():
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    logger.error(
                        f"Error during shutdown of {event_name} task: {str(e)}"
                    )

        # shutdown executors
        for event_name, executor in self._executors.items():
            executor.shutdown(wait=True,)

        self._threads.clear()
        self._executors.clear()
        self._active_futures.clear()