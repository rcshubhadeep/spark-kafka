import fire

from tkf.adapters.consumers.consumer import get_consumer


def consume_data(consumer_type='spark_avro', topic_name='test'):
    ac = get_consumer(consumer_type,
                      'localhost:9092',
                      [topic_name],
                      app_name='SimpleSpark')
    ac.start_consuming()


if __name__ == "__main__":
    fire.Fire(consume_data)
