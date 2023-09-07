"""
## Question 4:

Write a Python program to find the list in a list of lists whose sum of elements is the highest.

**Sample Input:**

```python
Input: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Output: [10, 11, 12]
```
"""

# Code:

# Method-1 (Using nested for loop)

def highest_sum(list1):
    max_sum = 0
    for i in list1:
        sum = 0
        for j in i:
            sum += j
        if sum > max_sum:
            max_sum = sum
            max_list = i
    return max_list


list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
list1 = highest_sum(list1)
print("The list with highest sum is : ", list1)


#------------------------------------------------------------------------

# Method-2 (Using list comprehension)

list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

max_list = max(list1, key=lambda i: sum(i))
print("The list with highest sum is : ", max_list)
