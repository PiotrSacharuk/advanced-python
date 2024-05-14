def func(a, b):
    return a + b


a = 0
for _ in range(100000000):
    a += func(3, 5)
print(a)
