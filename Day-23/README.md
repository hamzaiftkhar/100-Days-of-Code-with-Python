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