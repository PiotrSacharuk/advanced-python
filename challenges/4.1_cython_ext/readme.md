# Python Coding Challenge: Implementing and Benchmarking a Cython Function

## Background:
Cython is a programming language that makes writing C extensions for Python as easy as writing Python itself. It's particularly effective for speeding up CPU-bound tasks that involve loops, numerical computations, and more detailed type definitions.

## Task:
Your task is to implement a function in Cython that calculates the sum of squares for a large list of integers, and then compare the performance of this Cython implementation with a pure Python implementation.

## Steps to Complete the Challenge:

1. Setup Environment:

* Ensure you have Cython installed (pip install cython).
* You will also need a C compiler installed on your system.

2. Create a Python Function (Baseline):

* Write a Python function to compute the sum of squares of a list of integers.
python

3. Implement the Function in Cython:

* Create a Cython file (sum_of_squares.pyx) to implement the same functionality.
cython
* Write a setup file (setup.py) to compile the Cython code
* Compile the Cython module by running python setup.py build_ext --inplace in the command line.

4. Benchmark Both Implementations:
* Use a large list of integers to test both the Python and Cython functions.
* Measure the execution time using timeit module.
python

5. Compare and Analyze Results:

* Compare the execution times of the Python and Cython implementations.
* Discuss why the Cython version is faster or slower based on your observations.

## Challenge Goals:

* Implement and compile a Cython function.
* Measure and compare the performance of a pure Python implementation versus a Cython implementation.
* Understand how Cython can be used to speed up numerical computations in Python.