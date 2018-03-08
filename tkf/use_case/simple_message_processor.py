import json


class SimpleMessageProcessor(object):

    @classmethod
    def process_message(cls, msg_str):
        return json.loads(msg_str)
