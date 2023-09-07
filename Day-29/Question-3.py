"""
## Question 3:

Given a list of tuples, write a Python program to sort the tuples alphabetically by the first item of each tuple.

**Sample Input:**

```python
Input: [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
Output: [('Amana', 28), ('Abhishek', 29), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
```
"""

# Code:

# Method-1 (Using nested for loop)
def sort_tuples(list1):
  for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
      if list1[i][0] > list1[j][0]:
        list1[i], list1[j] = list1[j], list1[i]
  return list1

list1 = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
print("The original list is : ", list1)

list1 = sort_tuples(list1)
print("The sorted list is : ", list1)

"""
- This program works by first iterating through the list twice. The first iteration is to find all the pairs of tuples that are out of order. The second iteration is to swap the order of the tuples in the pair.

- The for i in range(len(list1)): loop iterates through the list and assigns each tuple to the variable i.

- The for j in range(i + 1, len(list1)): loop iterates through the list starting from the element after i.

- The if list1[i][0] > list1[j][0] statement checks if the first item of the tuple at index i is greater than the first item of the tuple at index j. If it is, then the two tuples are out of order and their order is swapped.

- Finally, the function returns the sorted list of tuples.
"""

# Method-2 (Using lambda function)
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[0])


tuples = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

print("The original list is : ", sort_tuples(tuples))
