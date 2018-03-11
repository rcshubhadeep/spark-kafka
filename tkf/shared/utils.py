import os
import time


def current_time_in_millis():
    return int(round(time.time() * 1000))


def get_project_dir():
    proj_path = os.path.dirname(os.path.abspath(__file__)).split('/')
    return '/'.join(proj_path[:-2]) + '/avro_schemas/{}'
