"""
## Question 4

Given three sets A, B, and C, write a Python function that determines whether C is a subset of both A and B simultaneously.

For example:

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {3, 4}
```

The function should return True because C is a subset of both A and B.

"""

# Solution:

def is_subset(set1, set2, set3):
    # Check if set3 is a subset of set1 and set2
    if set3.issubset(set1) and set3.issubset(set2):
        return True
    else:
        return False
    
# Example usage:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {3, 4}

result = is_subset(A, B, C)
print(result)

# Output:
# True

"""
EXPLANATION:-

Here's a step-by-step explanation:

1. Check if set3 is a subset of set1 and set2
2. Return the result

"""