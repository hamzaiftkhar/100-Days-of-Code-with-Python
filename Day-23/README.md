# Introduction to Lists in Python Programming

## What is a List?

A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

Lists are great to use when you want to work with many related values. They enable you to keep data together that belongs together, condense your code, and perform the same methods and operations on multiple values at once.

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

Syntax
```python
list_name = [item_1, item_2, item_3]
```

## Creating a List

Lists are created using square brackets [ ] with commas separating items.

The list contains different data types like integer, float, string, etc.

```python
# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)
```

Output
```python
[]
[1, 2, 3]
[1, 'Hello', 3.4]
```

- Time Complexity: **O(1).**
- Space Complexity: **O(n).**

## Accessing Elements in a List

There are various ways in which we can access the elements of a list.

In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing.

- **Positive Indexing:** Starts from 0 from the left side of the list.

```python
# Python program to demonstrate
# accessing of element from list

# Creating a List with
# the use of multiple values
List = ["100-Days", "of", "Code"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
```

Output
```python
Accessing a element from the list    
100-Days    #print(List[0])
Code        #print(List[2])
```

- **Negative Indexing:** In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

```python
List = [1, 2, '100-Days', 4, 'of', 6, 'Code']

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])
```

Output

```python
Accessing element using negative indexing
Code    #print(List[-1])
of      #print(List[-3])
```

Complexities for Accessing elements in a Lists:

- Time Complexity: **O(1).**
- Space Complexity: **O(1).**

## Getting the size of Python list

To get the size of a Python list, we can use the built-in function len(). It returns the number of elements in a list.

```python
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))
```

Output

```python
0
3
```