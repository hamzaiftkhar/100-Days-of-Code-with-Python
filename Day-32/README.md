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

## Frozen Sets

Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).

Frozen sets can be created by using the function frozenset().

This type of sets supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

```python
# Python program to demonstrate
# working of a FrozenSet

# Creating a Set
String = ('P', 'y', 't', 'h', 'o', 'n')
Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet is: ")
print(frozenset())
```

```python
The FrozenSet is:
frozenset({'y', 'o', 't', 'P', 'n', 'h'})

Empty FrozenSet is:
frozenset()
```

## Advantages of Sets in Python

- **Unique Elements:** Sets can only contain unique elements, so they can be useful for removing duplicates from a collection of data.
- **Fast Membership Testing:** Sets are optimized for fast membership testing, so they can be useful for determining whether a value is in a collection or not.
- **Mathematical Set Operations:** Sets support mathematical set operations like union, intersection, and difference, which can be useful for working with sets of data.
- **Mutable:** Sets are mutable, which means that you can add or remove elements from a set after it has been created.

## Disadvantages of Sets in Python

- **Unordered:** Sets are unordered, which means that you cannot rely on the order of the data in the set. This can make it difficult to access or process data in a specific order.
- **Limited Functionality:** Sets have limited functionality compared to lists, as they do not support methods like append() or pop(). This can make it more difficult to modify or manipulate data stored in a set.
- **Memory Usage:** Sets can consume more memory than lists, especially for small datasets. This is because each element in a set requires additional memory to store a hash value.
- **Less Commonly Used:** Sets are less commonly used than lists and dictionaries in Python, which means that there may be fewer resources or libraries available for working with them. This can make it more difficult to find solutions to problems or to get help with debugging.

## Important Note:

In Python, sets do not produce shuffled output by design. Sets are unordered collections of unique elements, which means they do not have a specific order, and the elements are not arranged in any particular sequence. When you iterate through a set or print its elements, the order in which the elements are displayed may appear shuffled, but it is not intentional randomness.

The apparent randomness in the order of elements in a set is due to the way Python's sets are implemented internally. Sets use hash tables (also known as dictionaries) to store their elements for efficient membership testing and elimination of duplicates. Hash tables do not guarantee any specific order when you iterate through their keys or values.

If you need a collection that maintains the order of elements, you can use a list or another ordered data structure like collections.OrderedDict (for Python 3.1 and later) or collections.OrderedDict (for Python 2.7 and 3.0). These data structures preserve the order in which elements are added, allowing you to access and iterate through the elements in a predictable order.