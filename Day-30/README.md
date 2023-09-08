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

## Adding elements to a Dictionary

In Python Dictionary, addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key **e.g. Dict[Key] = ‘Value’**. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary.

**Note-** While adding a value, if the key value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.

```python
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Python'
Dict[2] = 'Coding'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Python', '2': 'Programming'}}
print("\nAdding a Nested Key: ")
print(Dict)
```

Output:

```python
Empty Dictionary: 
{}

Dictionary after adding 3 elements: 
{0: 'Python', 2: 'Coding', 3: 1}

Dictionary after adding 3 elements: 
{0: 'Python', 2: 'Coding', 3: 1, 'Value_set': (2, 3, 4)}

Updated key value: 
{0: 'Python', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}

Adding a Nested Key: 
{0: 'Python', 2: 'Welcome', 3: 1, 5: 'Value_set': (2, 3, 4) : {'Nested': {'1': 'Python', '2': 'Programming'}}}
```

**Complexities for Adding elements in a Dictionary:**

- Time complexity: **O(1)/O(n)**

- Space complexity: **O(1)**

## Accessing elements from a Dictionary

In order to access the items of a dictionary refer to its key name.Key can be used inside square brackets.

There is also a method called get() that will also help in acessing the element from a dictionary.

```python
# Python program to demonstrate
# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Python', 'name': 'is', 3: 'Fun'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])
```

Output:

```python
Accessing a element using key:
is

Accessing a element using key:
Python
```

Accessing element using get():

```python
# Creating a Dictionary
Dict = {1: 'Python', 'name': 'is', 3: 'Fun'}

# accessing a element using get() method
print("Accessing a element using get:")
print(Dict.get(3))
```

Output:

```python
Accessing a element using get:
Fun
```

- ### Acessing element of a nested dictionary

In order to access the value of any key in nested dictionary, use indexing [] syntax.

```python
# Creating a Dictionary
Dict = {'Dict1': {1: 'Python'},
        'Dict2': {'Name': 'Program'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
```

Output:

```python
{1: 'Python'}
Python
Program
```

**Complexities for Accessing elements in a Dictionary:**

- Time complexity: **O(1)**

- Space complexity: **O(1)**

## Removing Elements from Dictionary

In Python Dictionary, deletion of keys can be done by using the del keyword. Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted. Items in a Nested dictionary can also be deleted by using del keyword and providing specific nested key and particular key to be deleted from that nested Dictionary.

```python
# Python program to demonstrate
# Deleting Elements using del Keyword

# Creating a Dictionary
Dict = {1: 'Python', 'name': 'is', 3: 'Fun'}

print("Dictionary =")
print(Dict)
#Deleting some of the Dictionary data
del(Dict[1])
print("Data after deletion Dictionary=")
print(Dict)
```

Output:

```python
Dictionary =
{1: 'Python', 'name': 'is', 3: 'Fun'}
Data after deletion Dictionary=
{'name': 'is', 3: 'Fun'}
```

## Looping through a Dictionary

We can loop through a dictionary by using a for loop. When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

```python
# Python program to loop through dictionary
# Creating a Dictionary
Dict = {1: 'Python', 'name': 'is', 3: 'Fun'}

# Iterating through a Dictionary
for Key, Value in Dict.items():
    print(Key, Value)
```

Output:

```python
1 Python
name is
3 Fun
```