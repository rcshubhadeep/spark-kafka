from tkf.adapters.producers.avro_producer import AvroProducerAdapter
from tkf.adapters.producers.simple_producer import SimpleProducerAdapter


def get_producer(topic, producer_type='avro', **kwargs):
    if producer_type == 'avro':
        return AvroProducerAdapter(topic=topic, **kwargs)
    else:
        return SimpleProducerAdapter(topic=topic)
