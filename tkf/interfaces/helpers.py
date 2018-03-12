from typing import Any, Tuple

import random


def choose_randomly_from(data: Any) -> Tuple[Any, Any]:
    """Helper function. Very local to interfaces.
    Especially how producers work presently.

    Thus it is not a part of shared

    """
    if isinstance(data, dict):
        keys = list(data.keys())
        random_index = random.randint(0, len(keys) - 1)
        random_key = keys[random_index]
        return (random_key, data[random_key])
    elif isinstance(data, list):
        random_index = random.randint(0, len(data) - 1)
        return (data[random_index], None)
