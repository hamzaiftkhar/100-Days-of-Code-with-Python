"""
( optional question we will better understand it when we learn lists comprehensions)

Question-3:
We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

Test Data:

Input: 2
Output:
[2, 4]

Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

input: 5
Output:
[5, 7, 9, 11, 13]
"""

# Code:

def find_stone_piles(n):
    start = n
    
    return [start + 2 * i for i in range(n)]   # List comprehension

# Test cases
test_cases = [2, 10, 5]

for n in test_cases:
    result = find_stone_piles(n)
    print(f"Input: {n}\nOutput: {result}\n")