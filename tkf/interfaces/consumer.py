import fire

from tkf.adapters.consumers.consumer import get_consumer


def consume_data(consumer_type: str='spark_avro', topic_name: str='test', windowed: bool=True):
    """Main interface to start a consumer.

     It is called when we either run the bin/start_consumer.sh or manually
    run this script.

    Must be called using spark-submit unless the consumer_type is
    'avro' which should start a non-spark based consumer.

    Example spark-submit call

    > `spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 tkf/interfaces/consumer.py --consumer_type=simple_spark --topic_name=test2`

    Exposed to the outer world using the python-fire lib from
    Google.

    @TODO - make the function call match closely to producer and
    make the broker address and app_name dynamic as well.

    """
    ac = get_consumer(consumer_type,
                      'localhost:9092',
                      [topic_name],
                      app_name='SimpleSpark',
                      )
    ac.start_consuming(windowed=windowed)


if __name__ == "__main__":
    fire.Fire(consume_data)
