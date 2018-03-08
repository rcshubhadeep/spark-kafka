from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

BASE_PATH = "/home/shubadeep/kpler/pyproj/kafka-ex/exproj/avro_schemas/{}"

keys_schema_file = "keys.avsc"
values_schema_file = "values.avsc"


class AvroProducerAdapter(object):

    def __init__(self, key_name='ex-key', topic='test'):
        self.value_schema = avro.load(BASE_PATH.format(values_schema_file))
        self.avro_producer = AvroProducer({'bootstrap.servers': 'localhost:9092',
                                           'schema.registry.url': 'http://127.0.0.1:8081'},
                                          default_value_schema=self.value_schema)
        self.topic = topic

    def produce_message(self, val):
        self.avro_producer.produce(topic=self.topic, value=val)
        self.avro_producer.flush()
