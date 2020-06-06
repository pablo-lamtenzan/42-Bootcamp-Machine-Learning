import numpy as np


def cost(y, y_hat):
    if y.shape[0] != 1 or y.shape != y_hat.shape:
        return None
    return np.sum((np.power(y_hat - y, 2) / (2 * y.shape[0])) # normally should work

