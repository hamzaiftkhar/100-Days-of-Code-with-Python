"""
**Problem: Merge Lists and Find the Maximum Tuple Sum**

You are given two lists of tuples, list1 and list2. Each tuple in both lists contains two integers. Your task is to merge the two lists into a single list and find the maximum sum of the tuples that can be formed by selecting one tuple from each list. However, there's a catch: once you select a tuple from a list, you cannot select another tuple from the same list.

Write a Python function max_tuple_sum(list1, list2) that takes two lists of tuples as input and returns the maximum sum of the selected tuples.

**Sample Input:**

```python
list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [(7, 8), (9, 10), (11, 12)]

# Output should be 27
# Selecting (5, 6) from list1 and (11, 12) from list2 gives the maximum sum: 5 + 6 + 11 + 12 = 34
```

**Constraints:**

- Each list will contain at least one tuple.
- The length of both lists will be the same.
- The integers within each tuple will be non-negative.
"""

# Code:

def max_tuple_sum(list1, list2):
    max_sum = 0
    
    for tuple1 in list1:
        for tuple2 in list2:
            current_sum = sum(tuple1) + sum(tuple2)
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [(7, 8), (9, 10), (11, 12)]

result = max_tuple_sum(list1, list2)
print("The maximum sum of tuples is:", result)

#Output: The maximum sum of tuples is: 34

#------------------------------------------------------------