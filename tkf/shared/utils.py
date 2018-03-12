import os
import time


def current_time_in_millis() -> int:
    """Returns current time in millisecond since the epoch
    """
    return int(round(time.time() * 1000))


def get_project_dir() -> str:
    """Returns the base project dir.
    @TODO - can be improved

    """
    proj_path = os.path.dirname(os.path.abspath(__file__)).split('/')
    return '/'.join(proj_path[:-2])
