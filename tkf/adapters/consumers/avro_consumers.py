from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


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
