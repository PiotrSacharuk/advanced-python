discount_rate_global = 0.2


def calculate_discounted_price(price):
    """
    Calculate and print the discounted price of an item using a global discount rate.

    :param price: Original price of the item.
    :type price: float
    """
    global discount_rate_global
    discounted_price = price * (1 - discount_rate_global)
    print(f"The discounted price is: ${discounted_price:.2f}")
    return discounted_price


# Example usage:
# original_price = 100.0
# calculate_discounted_price(original_price)


def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers, modify the list in place,
    and print the result.

    :param numbers: List of numeric values.
    :type numbers: list of float or int
    :return: Sum of squares of the numbers.
    :rtype: float
    """
    for i in range(len(numbers)):
        numbers[i] **= 2  # Squaring each element in place
    total = sum(numbers)
    print(f"The sum of squares (impure) is: {total}")
    return total


# Example usage:
# numbers_list = [1, 2, 3, 4]
# result = sum_of_squares(numbers_list)
# print(f"The sum of squares is: {result}")
# print(f"Modified list after function call: {numbers_list}")
