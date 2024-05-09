
def custom_generator():
    n = 0
    while True:
        yield (3*n-1)/2
        n += 1


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b


obj = custom_generator()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# for x in obj:
#     print(x)
