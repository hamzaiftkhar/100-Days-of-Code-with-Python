# Exploring Python String Manipulation: Indexing, Slicing, and Essential Methods

The Python string data type is a sequence made up of one or more individual characters that could consist of letters, numbers, whitespace characters, or symbols. As the string is a sequence, it can be accessed in the same ways that other sequence-based data types are, through indexing and slicing.

## Indexing
Indexing means referring to an element of an iterable by its position within the iterable. Each of a string’s characters corresponds to an index number and each character can be accessed using its index number. We can access characters in a String in Two ways :

- Accessing Characters by Positive Index Number
- Accessing Characters by Negative Index Number

#### 1. Accessing Characters by Positive Index Number:
 In this type of Indexing, we pass a Positive index(which we want to access) in square brackets. The index number starts from index number 0 (which denotes the first character of a string).

```python
# Python program to demonstrate
# accessing of characters in a string

str = "python"
print("str = ", str)

#first character
print("str[0] = ", str[0])

#third character
print("str[2] = ", str[2])

```
Output:
```python
str =  python
str[0] =  p
str[2] =  t
```
#### 2. Accessing Characters by Negative Index Number:

In this type of Indexing, we pass the Negative index(which we want to access) in square brackets. Here the index number starts from index number -1 (which denotes the last character of a string).
    
```python
# Python program to demonstrate
# accessing of characters in a string

str = "python"

#last character
print("str[-1] = ", str[-1])

#3rd last character
print("str[-3] = ", str[-3])
```
Output:
```python
str[-1] =  n
str[-3] =  h
```