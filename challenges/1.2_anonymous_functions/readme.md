# Coding Challenge: One-Line Functional Transformation

## Background:
Lambda functions in Python are small anonymous functions defined with the lambda keyword. map, filter, and reduce are fundamental functional programming tools that apply functions to sequences and collections.

## Challenge Description:
You are provided with a list of integers. Your task is to write a single line of Python code using lambda functions with map, filter, and reduce to perform a sequence of operations that transforms this list into a single output value.

## Task Requirements:
1. Filter the list to include only even numbers.
2. Map these even numbers to their squares.
3. Reduce these squares to their sum.

Example List:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected Outcome:
For the list given above, the transformation should follow these steps:

* Filter to even numbers: [2, 4, 6, 8, 10]
* Map to squares: [4, 16, 36, 64, 100]
* Reduce to sum of squares: 220

## Python Code Challenge:

Write a single line of Python code that implements the sequence of operations described above using lambda functions and the map, filter, and reduce functions. You must import the necessary module(s) for reduce.

## Instructions:

1. Understand how each function (map, filter, reduce) works and how they can be combined.
2. Use anonymous functions (lambda) efficiently to perform the operations in a concise manner.
3. Ensure that your one-liner code is readable and follows Python's best practices for lambda functions.

## Additional Tips:

* Remember that readability is key in Python, and while one-liners can be elegant, they should not compromise understanding.
* Test your function with different lists to ensure it works universally for similar tasks.