# Fourth Exercise Solution and Additional Resources

## Question 1:

Write a Python Program that Sorts Lists Within List in reverse order.

**Sample Input:**

```python
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
```

- [Solution to Question 1]()

## Question 2:

Write Python Program to print duplicates from a list of integers?

The task is to generate another list, which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

**Sample Input:**

```python
Input : list = [2, 4, 10, 20, 5, 2, 20, 4]
Output : list = [2, 4, 20]
```

- [Solution to Question 2]()

## Question 3:

Given a list of tuples, write a Python program to sort the tuples alphabetically by the first item of each tuple.

**Sample Input:**

```python
Input: [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
Output: [('Amana', 28), ('Abhishek', 29), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
```

- [Solution to Question 3]()

## Question 4:

Write a Python program to find the list in a list of lists whose sum of elements is the highest.

**Sample Input:**

```python
Input: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Output: [10, 11, 12]
```

- [Solution to Question 4]()

## Question 5:

**Problem: Merge Lists and Find the Maximum Tuple Sum**

You are given two lists of tuples, list1 and list2. Each tuple in both lists contains two integers. Your task is to merge the two lists into a single list and find the maximum sum of the tuples that can be formed by selecting one tuple from each list. However, there's a catch: once you select a tuple from a list, you cannot select another tuple from the same list.

Write a Python function max_tuple_sum(list1, list2) that takes two lists of tuples as input and returns the maximum sum of the selected tuples.

**Sample Input:**

```python
list1 = [(1, 2), (3, 4), (5, 6)]
list2 = [(7, 8), (9, 10), (11, 12)]

# Output should be 27
# Selecting (3, 4) from list1 and (11, 12) from list2 gives the maximum sum: 3 + 4 + 11 + 12 = 27
```

**Constraints:**

- Each list will contain at least one tuple.
- The length of both lists will be the same.
- The integers within each tuple will be non-negative.

#### [Solution to Question 5]()