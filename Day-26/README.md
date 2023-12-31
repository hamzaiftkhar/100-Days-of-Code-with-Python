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

## Tuples Items - Data Types

Tuples items can be of any data type: 

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

Output:

```python
('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)
```

A single tuple can contain different data types:

```python
tuple1 = ("Code", 34, True, 40, "Python")
print(tuple1)
```

Output:

```python
('Code', 34, True, 40, 'Python')
```

- ### Different types of tuples

A tuple can contain different data types in single tuple:

```python
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
```

Output:

```python
()
(1, 2, 3)
(1, 'Hello', 3.4)
```

## Accessing values in Python Tuples

Tuples in Python provide two ways by which we can access the elements of a tuple.

- ### Python Access Tuple using a Positive Index

Using square brackets we can get the values from tuples in Python.

```python
var = ("100", "-Days-of-", "Code")

print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])
```

Output:

```python
Value in Var[0] =  100
Value in Var[1] =  -Days-of-
Value in Var[2] =  Code
```

- ### Python Access Tuple using a Negative Index

In the above methods, we use the positive index to access the value in Python, and here we will use the negative index within [].

```python
var = ("100", "-Days-of-", "Code")

print("Value in Var[-1] = ", var[-1])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-3] = ", var[-3])
```

Output:

```python
Value in Var[-1] =  Code
Value in Var[-2] =  -Days-of-
Value in Var[-3] =  100
```

## Nested Tuples in Python

A tuple can contain another tuple as an element. This is called nested tuple.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.)

```python
# nested tuple
my_tuple = ("cartoon", [8, 4, 6], (1, 2, 3))
print(my_tuple)
```

Output:

```python
('cartoon', [8, 4, 6], (1, 2, 3))
```

## Create a Python Tuple With one Element

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

```python
var1 = ("Hello") # string
var2 = ("Hello",) # tuple

print(type(var1))
print(type(var2))
```

Output:

```python
<class 'str'>
<class 'tuple'>
```

Python 3.11 provides us with another way to create a tuple.

```python
values : tuple[int | str, ...] = (1,2,4,"Python")
print(values)
```

Output:

```python
(1, 2, 4, 'Python')
```

## Tuple Constructor in Python

It is also possible to use the tuple() constructor to make a tuple.

```python
var = tuple(("100", "-Days-of-", "Code"))
print(var)
```

Output:

```python
('100', '-Days-of-', 'Code')
```

Example:

```python
thistuple = tuple(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thistuple)
```

Output:

```python
('apple', 'banana', 'cherry')
```

## Advantages of Tuple over List in Python

Since tuples are quite similar to lists, both of them are used in similar situations.

However, there are certain advantages of implementing a tuple over a list:

- We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
- Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
- Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
- If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.