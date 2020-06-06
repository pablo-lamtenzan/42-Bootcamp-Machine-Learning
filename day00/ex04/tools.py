import numpy as np


def add_intercept(x):
    if len(x) == 0:
        return None
    # x has to be a np ndarray or return None
    ones = np.ones(x.shape[0], 1)
    ones.append(x)
    return ones
