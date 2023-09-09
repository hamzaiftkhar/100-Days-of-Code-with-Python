# Dictionary methods in Python Programming Language

Python Dictionary is like a map that is used to store data in the form of a key:value pair. Python provides various in-built functions to deal with dictionaries. In this Repository, we will see a list of all the functions provided by Python to work with dictionaries.

## Table of Python Dictionary Methods

| Function Name | Description                                                |
| ------------- | ---------------------------------------------------------- |
| clear()       | Removes all items from the dictionary                      |
| copy()        | Returns a shallow copy of the dictionary                   |
| fromkeys()    | Creates a dictionary from the given sequence               |
| get()         | Returns the value for the given key                        |
| items()       | Returns a list with all dictionary keys with values        |
| keys()        | Returns a view object that displays a list of all the keys in the dictionary in order of insertion |
| pop()         | Returns and removes the element with the given key         |
| popitem()     | Returns and removes the key-value pair from the dictionary |
| setdefault()  | Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary |
| update()      | Updates the dictionary with the elements from another dictionary |
| values()      | Returns a list of all the values available in a given dictionary |

## Copying a Dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

### Example

Make a copy of a dictionary with the copy() method:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```

Output:

```python
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

Another way to make a copy is to use the built-in function dict().

### Example

Make a copy of a dictionary with the dict() function:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```

Output:

```python
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```