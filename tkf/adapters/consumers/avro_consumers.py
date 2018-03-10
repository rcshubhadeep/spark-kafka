from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient
from confluent_kafka.avro.serializer.message_serializer import MessageSerializer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from tkf.use_case.message_handler import (get_user_session_id,
                                          get_Visited_count
                                          )

schema_registry_client = CachedSchemaRegistryClient(url='http://127.0.0.1:8081')
serializer = MessageSerializer(schema_registry_client)


class AvroConsumerAdapter(object):

    def __init__(self, brokers='localhost:9092', topics=['test'], **kwargs):
        self.topics = topics
        self.consumer = AvroConsumer({'bootstrap.servers': brokers,
                                      'schema.registry.url': 'http://127.0.0.1:8081',
                                      'group.id': 'mygroup',
                                      'auto.offset.reset': 'smallest'})
        self.consumer.subscribe(topics)

    def start_consuming(self):
        running = True
        while running:
            try:
                msg = self.consumer.poll(10)
                if msg:
                    if not msg.error():
                        print(msg.value())
                    elif msg.error().code() != KafkaError._PARTITION_EOF:
                        print(msg.error())
                        running = False
                    else:
                        print(msg.error())
            except SerializerError as e:
                print("Message deserialization failed for %s: %s" % (msg, e))
                running = False
            except Exception as ex:
                print(ex)
                running = False

        self.consumer.close()


class SparkAvroConsumerAdapater(object):

    def __init__(self, brokers, topics, **kwargs):
        self.app_name = kwargs['app_name']
        self.brokers = brokers
        self.topics = topics

    def start_consuming(self):
        sc = SparkContext(appName=self.app_name)
        sc.setLogLevel("WARN")
        ssc = StreamingContext(sc, 5)
        executor = KafkaUtils.createDirectStream(ssc,
                                                 self.topics,
                                                 {"metadata.broker.list": self.brokers},
                                                 valueDecoder=serializer.decode_message)
        lines = executor.map(lambda x: x[1])
        coockie_id_stream = lines.map(lambda x: get_user_session_id(x))
        count_normal = coockie_id_stream.countByValue()
        count_normal.pprint(5)
        count_windowed = coockie_id_stream.countByValueAndWindow(60, 5)
        count_windowed.pprint(5)

        check_pointed_context = StreamingContext.getOrCreate('/tmp/checkpoint_v01', lambda: ssc)
        check_pointed_context.start()
        check_pointed_context.awaitTermination()
