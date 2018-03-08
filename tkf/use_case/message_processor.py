from tkf.use_case.simple_message_processor import SimpleMessageProcessor


def get_message_processor(processor_type='simple'):
    if processor_type == 'simple':
        return SimpleMessageProcessor
