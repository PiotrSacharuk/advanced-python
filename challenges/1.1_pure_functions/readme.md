# Code Challenge: Convert an Impure Function to a Pure Function

## Background:

In programming, pure functions are a key component of functional programming. They must return the same output for the same input and should have no side effects (like modifying input arguments or interacting with external state).

## Challenge Description:

You are provided with a Python function that calculates the sum of all elements in a list after increasing each element by 10. However, the function is impure—it modifies the input list directly and prints the sum. Your task is to refactor this function into a pure function.

## Task:

Convert the above impure function into a pure function.
Ensure the function does not modify the input list.
Remove any side effects such as printing inside the function.
Return the total sum of the modified values without altering the original list.

## Expected Features in the Pure Function:

* Idempotence: Running the function any number of times with the same input should yield the same output every time.
* No External Interactions: The function should solely return a value and not interact with the outside world (no I/O operations).

## Instructions:

1. Clone the impure function and modify it to meet the criteria of a pure function.
2. Test your function to ensure it does not modify the original list and always returns the correct sum.
3. Optional: Write a few unit tests using Python's unittest or pytest to automatically check if your function behaves as expected with various inputs.

## Additional Tips:

* Use list comprehensions or the map function to create a new list with the updated values.
* Consider the impact of your changes on the function's performance and usability.