# Python Coding Challenge: Optimizing a Prime-Checking Function with Cython


## Background:
The is_prime function is a typical example of a CPU-bound task that can benefit significantly from Cython’s optimizations, such as compiling to C, type declarations, and avoiding some of Python's overhead.

## Task:
Convert the provided Python is_prime function to Cython, compile it, and compare its performance against the original Python version. The goal is to demonstrate the performance benefits of using Cython for computational heavy tasks.

## Steps to Complete the Challenge:

1. Python Function (Baseline):
Start by reviewing the pure Python implementation of the is_prime function.
python
2. Setup Cython Environment:
   * Ensure Cython is installed.
   * You will also need a C compiler setup as previously described.
3. Create & compile the Cython Function:
   * Write the Cython version of the is_prime function in a .pyx file. Use type declarations to improve performance.
   * Create a setup.py file for compiling the Cython code:
    ```python
    from setuptools import setup
    from Cython.Build import cythonize

    setup(
        ext_modules = cythonize("prime_check.pyx")
    )
    ```
   * Compile the Cython module by running python setup.py build_ext --inplace.
4. Benchmarking:
   * Use a large set of numbers to test both the Python and Cython functions using the timeit module.
5. Compare and Analyze Results:
   * Discuss the performance of the Python vs. Cython implementation.
   * Evaluate how effectively type declarations and Cython optimizations improved the function.

## Challenge Goals:
* Understand how to convert Python code into Cython for performance improvements.
* Learn how to set up and compile Cython modules.
* Demonstrate the potential speed gains from using Cython, especially in computational tasks.