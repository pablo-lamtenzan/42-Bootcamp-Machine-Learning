import numpy as np

def simple_predict(x, theta):
    if len(x) == 0 or len(theta) == 0:
        return None
    if x.shape[1] != 1 or theta.shape != (2, 1):
        return None
    y_hat = np.zeros(x.shape[0])
    for i in range(len(x)):
        y_hat[i] = theta[0] + (theta[1] * x[i])
    return y_hat
