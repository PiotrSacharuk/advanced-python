# Coding Challenge: Tribonacci Sequence Generator

## Background:
In the Tribonacci sequence:
𝑇(0)=0,𝑇(1)=1,𝑇(2)=1
𝑇(𝑛)=𝑇(𝑛−1)+𝑇(𝑛−2)+𝑇(𝑛−3) for 𝑛≥3

## Challenge Description:
Your task is to write a generator function that yields the Tribonacci sequence up to n terms. The function should accept a single argument, n, which specifies the number of terms to generate.

## Requirements:
Create a generator function named tribonacci_generator that yields the Tribonacci sequence up to n terms.
The generator should produce numbers one at a time, on demand.
If n is less than or equal to 0, the generator should yield nothing.
Use the generator function in a loop to print the generated sequence.

Expected Output:
The first 10 terms of the Tribonacci sequence:
0
1
1
2
4
7
13
24
44
81

## Instructions:
1. Implement the tribonacci_generator function according to the requirements.
2. Test the generator with different values of n to ensure it correctly handles edge cases like n = 0 and n = 1.
3. Check the performance of the generator with large values of n to observe the benefits of using a generator over a list.

## Goals of the Challenge:
* Practice creating and using generator functions in Python.
* Understand the memory efficiency of generators compared to traditional lists.
* Learn how to handle edge cases gracefully in generator functions.