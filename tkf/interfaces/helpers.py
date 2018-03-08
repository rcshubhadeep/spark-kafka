import random


def choose_randomly_from(data):
    if isinstance(data, dict):
        keys = list(data.keys())
        random_index = random.randint(0, len(keys) - 1)
        random_key = keys[random_index]
        return (random_key, data[random_key])
    elif isinstance(data, list):
        random_index = random.randint(0, len(data) - 1)
        return (data[random_index], None)
