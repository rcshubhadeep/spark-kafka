from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient
from confluent_kafka.avro.serializer.message_serializer import MessageSerializer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from tkf.use_case.message_handler import get_user_session_id

SCHEMA_REGISTRY_SERVER = 'http://127.0.0.1:8081'
# Construct a schema registry client. Will need to get avro schema while reading
schema_registry_client = CachedSchemaRegistryClient(url=SCHEMA_REGISTRY_SERVER)
serializer = MessageSerializer(schema_registry_client)


class AvroConsumerAdapter(object):
    """Simple and naive implementation of an avro consumer
    from a kafka stream.

    **Caution** - MUST not be used in production

    """

    def __init__(self,
                 brokers: str='localhost:9092',
                 topics: list=['test'],
                 **kwargs):
        self.topics = topics
        self.consumer = AvroConsumer({'bootstrap.servers': brokers,
                                      'schema.registry.url': SCHEMA_REGISTRY_SERVER,
                                      'group.id': 'mygroup',
                                      'auto.offset.reset': 'smallest'})
        self.consumer.subscribe(topics)

    def start_consuming(self, **kwargs):
        running = True
        while running:
            # Basic infinite while loop to listen to the topic and consume
            try:
                msg = self.consumer.poll(10)  # should be configurable
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

    def __init__(self, brokers: str, topics: list, **kwargs):
        self.app_name = kwargs['app_name']
        self.brokers = brokers
        self.topics = topics

    def start_consuming(self, **kwargs):
        """Kafka avro consumer from Spark.
        It can be configured to run a simple consumer or a sliding window based consumer

        """
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
        if kwargs['windowed'] is True:
            count_windowed = coockie_id_stream.countByValueAndWindow(60, 5)
            count_windowed.pprint(5)

        check_pointed_context = StreamingContext.getOrCreate('/tmp/checkpoint_v01', lambda: ssc)
        check_pointed_context.start()
        check_pointed_context.awaitTermination()
