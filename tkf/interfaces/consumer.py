from tkf.adapters.consumers.consumer import get_consumer


def run():
    ac = get_consumer('simple_spark', 'localhost:9092', ['test2'], app_name='SimpleSpark')
    ac.start_consuming()


if __name__ == "__main__":
    run()
