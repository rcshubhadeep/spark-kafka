import json


class SimpleMessageProcessor(object):
    """Implementation of a simple message processor.

    """
    @classmethod
    def process_message(cls, msg_str: str) -> dict:
        """Returns a python dict from the incoming json string

        """
        return json.loads(msg_str)

    @classmethod
    def sringify(cls, data: dict):
        return json.dumps(data)
