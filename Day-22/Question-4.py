"""
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

Write a Python program to print the Fibonacci sequence up to n-th term using recursive function.

Test Data:

Input: 5
Output: 0 1 1 2 3   

Input: 10
Output: 0 1 1 2 3 5 8 13 21 34
"""

# Code:

def fibonacci_loop(n):
    a, b = 0, 1
    count = 0
    
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

fibonacci_loop(10)
