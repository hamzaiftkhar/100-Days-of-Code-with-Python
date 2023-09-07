"""
## Question 2:

Write Python Program to print duplicates from a list of integers?

The task is to generate another list, which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

**Sample Input:**

```python
Input : list = [2, 4, 10, 20, 5, 2, 20, 4]
Output : list = [2, 4, 20]
```
"""

# Code:

def find_duplicates(list1):
  duplicates = []
  for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
      if list1[i] == list1[j]:
        duplicates.append(list1[i])
        break
  return duplicates

list1 = [2, 4, 10, 20, 5, 2, 20, 4]
print("The original list is : ", list1)

duplicates = find_duplicates(list1)
print("The duplicate elements are : ", duplicates)

# Input:
# [2, 4, 10, 20, 5, 2, 20, 4]

# Output:
# The original list is :  [2, 4, 10, 20, 5, 2, 20, 4]
# The duplicate elements are :  [2, 4, 20]