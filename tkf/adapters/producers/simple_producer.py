from confluent_kafka import Producer

from tkf.use_case.message_processor import get_message_processor


class SimpleProducerAdapter(object):

    def __init__(self, key_name: str='ex-key', topic: str='test'):
        self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
        self.topic = topic
        self.msg_prcr = get_message_processor()

    def produce_message(self, val: dict):
        data = self.msg_prcr.sringify(val)
        self.producer.produce(topic=self.topic, value=data.encode('utf-8'))
        self.producer.flush()
