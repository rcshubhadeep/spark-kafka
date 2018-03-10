from tkf.adapters.consumers.consumer import get_consumer


def consume_data():
    ac = get_consumer('spark_avro', 'localhost:9092', ['test'], app_name='SimpleSpark')
    ac.start_consuming()


if __name__ == "__main__":
    consume_data()
