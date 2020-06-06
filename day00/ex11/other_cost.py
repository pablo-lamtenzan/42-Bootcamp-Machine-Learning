import numpy as np
import math


def mse(y, y_hat):
    if y.shape[1] != 1 or y.shape != y_hat.shape:
        return None
    return np.mean(np.power(y_hat - y, 2))

def rmse(y, y_hat):
    return math.sqrt(mse(y, y_hat))

def mae(y, y_hat):
    if y.shape[1] != 1 or y.shape != y_hat.shape:
        return None
    return np.mean(np.absolute(y_hat - y))

def r2score(y, y_hat):
    if y.shape[1] != 1 or y.shape != y_hat.shape:
        return None
    return 1 - (np.sum(np.power(y_hat - y, 2)) / (np.sum(np.power(y_hat - mean(y), 2))))
