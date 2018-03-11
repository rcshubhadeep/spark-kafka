import time

import fire

from tkf.adapters.producers.producer import get_producer
from tkf.interfaces.helpers import choose_randomly_from
from tkf.shared.utils import current_time_in_millis, get_project_dir

BASE_PATH = get_project_dir()
values_schema_file = "values.avsc"

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


def produce_data(producer_type='avro', topic_name='test'):
    avro_file = BASE_PATH.format(values_schema_file)
    prdcr = get_producer(topic_name, producer_type=producer_type, value_schmea_loc=avro_file)
    while True:
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
