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

## Adding Elements to a Set

- **Using add() method**

Elements can be added to the Set by using built-in add() function. Only one element at a time can be added to the set by using add() method, loops are used to add multiple elements at a time with the use of add() method.

```python
# Creating a Set
set1 = set()
print("Intial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)
```

```python
Intial blank Set:
set()

Set after Addition of Three elements:
{8, 9, (6, 7)}

Set after Addition of elements from 1-5:
{1, 2, 3, 4, 5, 6, 7, 8, 9, (6, 7)}
```

- **Using update() method**

For addition of two or more elements Update() method is used. The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

```python
# Addition of elements to the Set
# using Update function
set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
```

```python
Set after Addition of elements using Update:
{4, 5, 10, 11, (6, 7)}
```

## Accessing a Set

Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

```python
# Creating a set
set1 = set(["Python", "For", "Everyone"])
print("\nInitial set")
print(set1)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
```

```python
Initial set
{'Everyone', 'For', 'Python'}

Elements of set:
Everyone For Python
```

## Removing elements from the Set

- **Using remove() method or discard() method**

Elements can be removed from the Set by using built-in remove() function but a KeyError arises if element doesn’t exist in the set. To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged.

```python
# Creating a set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Intial Set: ")
print(set1)

# Removing elements from Set
# using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set
# using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)
```

```python
Intial Set:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Set after Removal of two elements:
{1, 2, 3, 4, 7, 8, 9, 10, 11, 12}

Set after Discarding two elements:
{1, 2, 3, 4, 7, 10, 11, 12}
```

- **Using pop() method**

Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set.

```python
# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Intial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)
```

```python
Intial Set:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Set after popping an element:
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
```

- **Using clear() method**

To remove all the elements from the set, clear() function is used.

```python
# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Intial Set: ")
print(set1)

# Removing all the elements from
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)
```

```python
Intial Set:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

Set after clearing all the elements:
set()
```