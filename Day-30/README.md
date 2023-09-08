# Introduction to Dictionaries in Python

## What is a Dictionary?

A dictionary is a collection of key-value pairs. A dictionary is a set of key-value pairs, where each key is unique and is used to access a corresponding value. Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

**Note** - Unlike other data types that hold only one value as an element, a dictionary holds a key:value pair. The key is the element that is used to access the value, and it must be unique. A dictionary is mutable, which means it can be changed. The values that the keys point to can be any Python value.

 Dictionaries are unordered, so the order that the keys are added doesn’t necessarily reflect what order they may be reported back.

```python
Dict = {1: 'Code', 2: 'with', 3: 'Python'}
print(Dict)
```

Output: 

```python
{1: 'Code', 2: 'with', 3: 'Python'}
```

## Creating a Dictionary

In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.

Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.

```python
# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Code', 2: 'with', 3: 'Python'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Python', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
```

Output:

```python
Dictionary with the use of Integer Keys: 
{1: 'Code', 2: 'with', 3: 'Python'}

Dictionary with the use of Mixed Keys: 
{'Name': 'Python', 1: [1, 2, 3, 4]}

Dictionary with each item as a pair: 
{1: 'Geeks', 2: 'For'}
```

**Complexities for creating a dictionary in Python :**

- Time complexity: **O(len(dict))**

- Space complexity: **O(n)**