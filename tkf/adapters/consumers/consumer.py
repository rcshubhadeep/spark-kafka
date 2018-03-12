from tkf.adapters.consumers.avro_consumers import AvroConsumerAdapter, SparkAvroConsumerAdapater
from tkf.adapters.consumers.simple_spark_consumer import SimpleSparkConsumerAdapter


def get_consumer(consumer_type: str, brokers: list, topics: list, **kwargs) -> object:
    """Factory method to get right type of consumer.

    Available options -

    *) avro
    *) spark_simple
    *) spark_avro

    """
    if consumer_type == 'avro':
        return AvroConsumerAdapter(brokers=brokers, topics=topics)
    elif consumer_type == 'spark_simple':
        return SimpleSparkConsumerAdapter(brokers=brokers, topics=topics, **kwargs)
    elif consumer_type == "spark_avro":
        return SparkAvroConsumerAdapater(brokers=brokers, topics=topics, **kwargs)
