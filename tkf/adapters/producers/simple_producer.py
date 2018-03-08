import json

from confluent_kafka import Producer


class SimpleProducerAdapter(object):

    def __init__(self, key_name='ex-key', topic='test'):
        self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
        self.topic = topic

    def produce_message(self, val):
        data = json.dumps(val)
        self.producer.produce(topic=self.topic, value=data.encode('utf-8'))
        self.producer.flush()
