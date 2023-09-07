"""
## Question 1:

Write a Python Program that Sorts Lists Within List in reverse order.

**Sample Input:**

```python
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
```
"""

# Code:

def reverse_sort(list1):
  for i in range(len(list1)):
    list1[i].reverse()
  return list1

list1 = [[4, 1, 6], [7, 8], [4, 10, 8]]
print("The original list is : ", list1)

list1 = reverse_sort(list1)
print("The reverse sorted Matrix is : ", list1)

# Input:
# [[4, 1, 6], [7, 8], [4, 10, 8]]

# Output:
# The original list is :  [[4, 1, 6], [7, 8], [4, 10, 8]]
# The reverse sorted Matrix is :  [[6, 4, 1], [8, 7], [10, 8, 4]]