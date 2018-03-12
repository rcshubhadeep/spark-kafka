import time

import fire

from tkf.adapters.producers.producer import get_producer
from tkf.interfaces.helpers import choose_randomly_from
from tkf.shared.utils import current_time_in_millis, get_project_dir

# we get the project root dir here and then append the avro_shemas
# with it.
# @TODO- replace with some kind of config management in future.
BASE_PATH = get_project_dir() + '/avro_schemas/{}'
values_schema_file = "values.avsc"

# Our dummy data. These will be randomly shuffled and used
# to produce visited events.
USERS = {'john': 'we0328nhe9t83', 'sid': '8905fjgf568', 'vasu': '342362hfg764r'}
TARGETS = ['http://example.com/home',
           'http://example.com/prodcuts/1/1',
           'http://example.com/prodcuts/1/5',
           'http://example.com/prodcuts/1/23',
           'http://example.com/prodcuts/1/2',
           'http://example.com/info',
           'http://example.com/carrer'
           ]
REFERRER = ['http://google.com',
            'http://linkedin.com',
            'http://stackoverflow.com',
            'http://faebook.com',
            'http://twitter.com'
            ]


def produce_data(producer_type: str='avro', topic_name: str='test') -> None:
    """Main interface function
    It is called when we either run the bin/start_producer.sh or manually
    run this script.

    Exposed to the outer world using the python-fire lib from
    Google.

    """
    avro_file = None
    if producer_type == 'avro':
        avro_file = BASE_PATH.format(values_schema_file)
    prdcr = get_producer(topic_name,
                         producer_type=producer_type,
                         value_schmea_loc=avro_file)
    while True:
        # Run indefinitely. Keep on producing a batch every 5 seconds
        print("Sending the next batch")
        for i in range(10):
            name, cid = choose_randomly_from(USERS)
            visited, _ = choose_randomly_from(TARGETS)
            refr, _ = choose_randomly_from(REFERRER)
            event_data = {"name": name,
                          "visted": visited,
                          "cookieid": cid,
                          "refered_from": refr,
                          "event_time": current_time_in_millis()}
            prdcr.produce_message(event_data)
        print("Sleeping for 5 seconds - *******")
        time.sleep(5)


if __name__ == "__main__":
    fire.Fire(produce_data)
