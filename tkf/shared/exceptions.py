from typing import Union


class BaseException(Exception):
    """Base Exception class. To be extended.

    """
    default_detail = 'Unknown Error'

    def __init__(self,
                 detail: Union[str, dict]=None) -> None:
        self.detail = self.default_detail if (detail is None) else detail


class NoAvroSchemaFileException(BaseException):
    default_detail = "Can not find the AVRO schema file"
