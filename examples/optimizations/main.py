from numba import jit


@jit(nopython=True)
def func(a, b):
    return a + b


@jit(nopython=True)
def run():
    a = 0
    for _ in range(100000000):
        a += func(3, 5)
    print(a)


run()
