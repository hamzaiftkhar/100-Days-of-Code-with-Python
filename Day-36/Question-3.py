"""
## Question 3

Write a Python function that takes two strings as input and returns a set containing all the characters that are common to both strings, ignoring spaces and case sensitivity.

For example:

```python
str1 = "Hello World"
str2 = "wonderful"
```

The function should return the set:

```python
{'o', 'l', 'r', 'd', 'w'}
```

"""

# Solution:

def common_characters(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Convert both strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find the intersection of the two sets
    common_chars = set1.intersection(set2)
    
    return common_chars

# Example usage:
str1 = "Hello World"
str2 = "wonderful"
result = common_characters(str1, str2)
print(result)

# Output:
# {'o', 'l', 'r', 'd', 'w'}

"""
EXPLANATION:-

Here's a step-by-step explanation:

1. Convert both strings to lowercase and remove spaces
2. Convert both strings to sets of characters
3. Find the intersection of the two sets
4. Return the result

"""
