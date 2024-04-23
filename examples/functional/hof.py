def convert_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f


# Example usage
# temperatures_celsius = [0, 10, 20, 30, 40, 50]
# temperatures_fahrenheit = list(map(convert_to_fahrenheit, temperatures_celsius))
# print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

def multiply(x, y):
    return x * y


# Example usage
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(multiply, numbers)
# print("The product of the list elements is:", product)


def is_even(x):
    if x % 2 == 0:
        return True
    return False


# Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(is_even, numbers))
# print("Even numbers in the list are:", even_numbers)