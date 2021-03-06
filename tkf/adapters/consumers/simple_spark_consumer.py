from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from tkf.use_case.message_processor import get_message_processor


class SimpleSparkConsumerAdapter(object):
    """Simple consumer of Kafka written in Spark.

    Does dot consume avro messages

    """

    def __init__(self, brokers: str, topics: list, **kwargs):
        self.app_name = kwargs['app_name']
        self.brokers = brokers
        self.topics = topics

    def start_consuming(self, **kwargs):
        sc = SparkContext(appName=self.app_name)
        ssc = StreamingContext(sc, 2)
        processor = get_message_processor()
        # createDirectStream is more suitable than
        # KafkaUtils.createStream. As it does not need any WAL support from
        # Spark's part.
        executor = KafkaUtils.createDirectStream(ssc,
                                                 self.topics,
                                                 {"metadata.broker.list": self.brokers})
        lines = executor.map(lambda x: processor.process_message(x[1]))
        # Sum up by unique identifier that we mapped in the step before.
        lines.count().map(lambda x: "There are {} number of messages in this batch".format(x)).\
            pprint()

        ssc.start()
        ssc.awaitTermination()
