def calculate_discounted_price(price, discount_rate):
    """
    Calculate the discounted price of an item based on the original price and discount rate.

    :param price: Original price of the item.
    :type price: float
    :param discount_rate: Discount rate (between 0 and 1).
    :type discount_rate: float
    :return: Discounted price.
    :rtype: float
    """
    discounted_price = price * (1 - discount_rate)
    return discounted_price


# Example usage:
# original_price = 100.0
# discount_rate = 0.2
# discounted_price = calculate_discounted_price(original_price, discount_rate)
# print(f"The discounted price is: ${discounted_price:.2f}")


def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    :param numbers: List of numeric values.
    :type numbers: list of float or int
    :return: Sum of squares of the numbers.
    :rtype: float
    """
    return sum(x ** 2 for x in numbers)


# Example usage:
# numbers_list = [1, 2, 3, 4]
# result = sum_of_squares(numbers_list)
# print(f"The sum of squares is: {result}")
