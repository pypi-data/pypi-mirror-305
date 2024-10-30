import random
import time

from fossa.control.message import TaskMessage
from fossa.tools.logging import LoggingMixin


class AbstractMycorrhiza(LoggingMixin):
    """
    A separate 'sidecar' process that is attached to the :class:`Governor` primarily to inject
    work tasks.

    The objective for sidecars is to (i) fetch details of sub-tasks that need to be run from an
    external source (e.g. a messaging service) (ii) send the sub-task to the governor to run
    and (iii) send results back to the originating task (iv) send log messages somewhere useful.

    The :meth:`run_forever` is executed in a separate process. It is provided with the governor's
    task queue onto which it submits subtasks. It is also provided with a shared variable used to
    indicate if the governor has capacity to accept additional work.

    Just before execution of the sidecar starts, the govenor will attach external logger modules
    if there are any. Log messages from sidecars are separate from the log messages generated
    by models.
    """

    def __init__(self):
        LoggingMixin.__init__(self)
        self.work_queue_submit = None
        self.available_processing_capacity = None

    def run_forever(self, work_queue_submit, available_processing_capacity):
        """
        Method to run in a separate process for the duration of Fossa.

        The arguments passed are for multiprocessing syncronisation. The Queue can't
        be passed as an argument to the constructor (sharedctype could) so keep them
        both together.

        These syncronisation variables are so subclasses of `AbstractMycorrhiza` can be partially
        attached to the governor.

        The entire governor object can't be passed as it contains weakrefs (multiprocessing Manger)
        so it can't be serialised.

        @param work_queue_submit: (Queue) end to send task into
        @param available_processing_capacity: sharedctypes int
        """
        raise NotImplementedError("Must be implemented by subclasses")

    @classmethod
    def submit_task(cls, task_spec, work_queue_submit, available_processing_capacity, timeout):
        """
        Wait for processing capacity in the governor then submit task for processing.

        @param task_spec: (TaskMessage)
        @param available_processing_capacity: (shared multiprocessing.Manager Value)
        @param timeout: float - max time before returning, will return after this but not exactly this.
        @return: bool - task was successfully passed to the governor's queue. Users of this method
                should re-try on False.
        """
        if not isinstance(task_spec, TaskMessage):
            raise ValueError("task_spec must be of type TaskMessage")

        # TODO - proper sync primitive in the governor
        # .qsize() isn't available on OSX, it's a proxy anyway so not worth pursuing
        # the empty check is enough for now to reduce the chance of running more
        # tasks then `available_processing_capacity`.

        timed_out = cls.wait_for_capacity(work_queue_submit, available_processing_capacity, timeout)
        if timed_out:
            # task not submitted
            return False

        work_queue_submit.put(task_spec)

        # reduce chance of race condition that see node allocated beyond capacity
        time.sleep(0.1)

        return True

    @classmethod
    def wait_for_capacity(cls, work_queue_submit, available_processing_capacity, timeout):
        """
        Block until the governor has capacity to process a task.

        Warning - potential race condition.

        @param available_processing_capacity: (shared multiprocessing.Manager Value)
        @param timeout: float - max time before returning, will return after this but not exactly this.
        @return: bool if timed out
        """
        # TODO - proper sync primitive in the governor
        start_time = time.time()
        while available_processing_capacity.value < 1 or not work_queue_submit.empty():
            collision_reduction = random.random()
            time.sleep(3.0 * collision_reduction)

            if (time.time() - start_time) > timeout:
                return True

        return False
