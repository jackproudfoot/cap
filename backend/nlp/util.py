import numpy as np


def shuffle_in_unison(*arrs):
    rng_state = np.random.get_state()
    for a in arrs:
        np.random.shuffle(a)
        np.random.set_state(rng_state)
