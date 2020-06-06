import numpy as np
from ../ex04.tools import add_intercept


def predict(x, theta):
    if len(x) == 0 or len(theta) == 0:
        return None
    if x.shape[1] != 1 or theta.shape != (2, 1):
        return None
    y_hat = np.zeros(x.shape[0])
    for i in range(len(x)):
        y_hat[i] = add_intercept(x[i]) * np.c_[theta] # that should work if np.c_[arg] rotates arg 90º
    return y_hat
