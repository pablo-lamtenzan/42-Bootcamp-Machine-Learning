import numpy as np


def cost_elems(y, y_hat):
    if y.shape[0] != 1 or y.shape != y_hat.shape:
        return None
    J_elems = np.zeros(y.shape)
    for i in range(y.shape[0]):
        J_elems[i] = (y_hat[i] - y[i]) ** 2 / (y.shape[0] * 2)
    return J_elems


def cost(y, y_hat):
    return sum(cost_elems(y, y_hat)) # if i did dump here is cause i have to take the sum AND THEN divide it and not each iteration mmm

