# Introduction to Tuples in Python Programming Language

## What is Tuple in Python?

Tuple is an ordered collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. The important difference between a list and a tuple is that tuples are immutable. Also, Tuples are hashable whereas lists are not.

Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

## Creating a Tuple

To create a tuple we will use () operators.
 
A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

Syntax:

```python
tuple_name = (item_1, item_2, item_3, ...)
```

Example:

```python
var = ("100", "Days-of", "Code")
print(var)
```

Output:

```python
('100', 'Days-of', 'Code')
```