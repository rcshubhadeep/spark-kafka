from tkf.adapters.producers.avro_producer import AvroProducerAdapter
from tkf.adapters.producers.simple_producer import SimpleProducerAdapter


def get_producer(topic: str, producer_type: str='avro', **kwargs) -> object:
    """Factory function to get right producer object

        Available options - 

        *) avro

        *) simple
    """
    if producer_type == 'avro':
        return AvroProducerAdapter(topic=topic, **kwargs)
    else:
        return SimpleProducerAdapter(topic=topic)
