import shutil
import logging
import os

from src._environment import Environment
from src._objects import JobStatus, ObjectType, Objects
from src.utils import FTBX_LOG_LEVELS
from rich.logging import RichHandler

# logger
logging.basicConfig(
    level=FTBX_LOG_LEVELS.get(os.getenv("FTBX_LOG_LEVEL", "INFO").upper()),
    format="%(name)s | %(message)s",
    handlers=[RichHandler()],
)
logger = logging.getLogger(__name__)


def clean_jobs_command_func(**kwargs) -> bool:
    """
    Clean the local directory of the environment's jobs that are no longer retriable (i.e. status: Completed, Cancelled).
    """
    logger.debug(f"Entering {__name__} with args: {kwargs}. ")
    environment = Environment.from_env_file(kwargs["from_"])
    logger.info(f'Starting clearing local jobs for environment "{environment.name}"')
    path_to_objects = os.path.join(environment.name, ObjectType.JOBS.value)
    object_dirs = os.listdir(path=path_to_objects)
    logger.debug(f"Jobs' folder: {object_dirs}")
    for object_dir in object_dirs:
        object_path = os.path.join(path_to_objects, object_dir)
        id = os.path.basename(object_path)
        logger.debug(f"Checking jobs ID: {id}")

        obj = Objects(
            object_type=ObjectType.JOBS,
            sub_items=[],
            filters={"id": id},
            save_results=False,
        )
        jobs = obj.get_from(environment=environment, log=logger.level == "DEBUG")
        # Handle case:
        if len(jobs) > 1:
            # Multiple jobs found for the given ID - Should not occur.
            logger.warning(f"Job ID: {id} returned more than one result. Skipping it.")
            continue
        elif len(jobs) == 0:
            # Job not found - I had this case while developping this feature.
            # My assumption is that Flex delete records of jobs in a certain status after an (unknown) amount of time.
            logger.warning(f"Job ID {id} not found - Deleting local orphean job folder")
            rmdir(object_path)
        else:
            job = jobs[0]
            # Not sure which status are "retriable", so I just delete local job folder if it is Cancelled or Completed.
            # This should cover 99% of use-case.
            if JobStatus.from_string(job.status) in [
                JobStatus.CANCELLED,
                JobStatus.COMPLETED,
            ]:
                rmdir(object_path)

    return True


def rmdir(relative_path: str):
    """
    Remove the given folder. Use with caution, no warning or confirmation before deletion.

    :param string: see argument `path` of `shutil.rmtree` for more detail
    """
    # os.rmdir(relative_path) - Does not work because folder is not empty.
    try:
        shutil.rmtree(relative_path)
    # shutil.rmtree has a race condition and can raise FileNotFound exception, which is a subclass of OSError.
    except OSError as err:
        logger.error(
            f"An exception occurred while trying to remove job's folder (ID:{id}) at: {relative_path}."
        )
        logger.error(err)
