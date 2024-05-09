from typing import TypeVar, Tuple

# Create a TypeVar, T, which can be any type
T = TypeVar('T')

def first_and_last(items: Tuple[T, ...]) -> Tuple[T, T]:
    """Returns the first and last item of a tuple, ensuring they are of the same type."""
    return items[0], items[-1]

def multiply(x: T, y: T) -> T:
    """Multiplies two items of the same type, which should support the multiplication operation."""
    return x * y


# Example usage:
a, b = first_and_last((3, 'a', True, 4.5, 5))
print(a, b)  # Output will be 3, 5

# This function call is valid if x and y are of the same type and support multiplication
result = multiply(10, 20)
print(result)  # Output will be 200

# This would also work for other data types supporting multiplication
result_float = multiply(2.5, 4.0)
print(result_float)  # Output will be 10.0
