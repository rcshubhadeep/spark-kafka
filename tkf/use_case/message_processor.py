from tkf.use_case.simple_message_processor import SimpleMessageProcessor


def get_message_processor(processor_type='simple'):
    """Factory function to get the right type of message processor

    """
    if processor_type == 'simple':
        return SimpleMessageProcessor
