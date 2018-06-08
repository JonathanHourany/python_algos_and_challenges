import random
from typing import AsyncGenerator


def online_reservoir_sampling(sample_size: int) -> AsyncGenerator[list, int]:

    count = 0
    sample = []

    while True:
        data = yield count, sample
        replace_idx = random.randint(0, count)

        if count < sample_size:
            sample.append(data)
        elif replace_idx < sample_size:
            sample[replace_idx] = data

        count += 1
