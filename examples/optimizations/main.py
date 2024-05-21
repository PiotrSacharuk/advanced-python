import time
# from numba import njit


# @njit
def func(a, b):
    return a + b


# @njit
def run():
    a = 0
    for _ in range(100000000):
        a += func(3, 5)
    print(a)

start = time.time()
run()
end = time.time()
print(end - start)

