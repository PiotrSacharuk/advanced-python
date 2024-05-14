import time

import numpy as np
# from numba import njit

# @njit
def some_func(n):
    z = np.zeros((n, n))
    for i in range(n):
        x = np.random.rand(n, n)
        y = np.random.rand(n, n)
        z += np.sqrt(x**2 + y**2)
    return z


start = time.time()
some_func(500)
end = time.time()
print(end-start)
