def increase_and_sum(numbers):
    """
    Increase each number in the list by 10, modify the list in place, and print the sum.
    This function is impure as it changes the input list and also prints within the function.

    :param numbers: List of numeric values.
    :type numbers: list of float or int
    """
    for i in range(len(numbers)):
        numbers[i] += 10
    total_sum = sum(numbers)
    print(f"Total sum: {total_sum}")
    return total_sum


# Example of impure usage:
nums = [1, 2, 3]
result = increase_and_sum(nums)
print(f"Modified list: {nums}")  # This will show the modified list
