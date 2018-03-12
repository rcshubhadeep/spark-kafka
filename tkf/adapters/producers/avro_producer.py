from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from tkf.shared.exceptions import NoAvroSchemaFileException


class AvroProducerAdapter(object):

    def __init__(self, value_schmea_loc: str=None,
                 key_nameL: str='ex-key',
                 topic: str='test'):
        if not value_schmea_loc:
            raise NoAvroSchemaFileException()
        self.value_schema = avro.load(value_schmea_loc)
        self.avro_producer = AvroProducer({'bootstrap.servers': 'localhost:9092',
                                           'schema.registry.url': 'http://127.0.0.1:8081'},
                                          default_value_schema=self.value_schema)
        self.topic = topic

    def produce_message(self, val: dict):
        """Write message in avro encoded format to Kafka topic

        """
        self.avro_producer.produce(topic=self.topic, value=val)
        self.avro_producer.flush()
