# Sets in Python Programming Language

## What are Sets in Python?

A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

However, the set itself is mutable. We can add or remove items from it.

Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by ‘comma’.

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

```python
{'cherry', 'apple', 'banana'}
```

## Creating a Set in Python

Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by ‘comma’.

```python
# Creating a Set
set1 = set()
print("Intial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("100-Days-of-Code-with-Python")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = '100-Days-of-Code-with-Python'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Python", "For", "Everyone"])
print("\nSet with the use of List: ")
print(set1)
```

```python
Intial blank Set:
set()

Set with the use of String:
{'-', 'n', 'h', 't', 'o', '1', 'w', 'i', 'e', 'y', '0', 'C', 'P', 'D', 's', 'f', 'r'}

Set with the use of an Object:
{'-', 'n', 'h', 't', 'o', '1', 'w', 'i', 'e', 'y', '0', 'C', 'P', 'D', 's', 'f', 'r'}

Set with the use of List:
{'Everyone', 'For', 'Python'}
```