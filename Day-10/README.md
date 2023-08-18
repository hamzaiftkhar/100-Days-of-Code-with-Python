# Exploring Python String Manipulation: Indexing, Slicing, and Essential Methods

The Python string data type is a sequence made up of one or more individual characters that could consist of letters, numbers, whitespace characters, or symbols. As the string is a sequence, it can be accessed in the same ways that other sequence-based data types are, through indexing and slicing.

## String Indexing 
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

## String Slicing

Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists. You can also use them to modify or delete the items of mutable sequences such as lists (later concept).

Syntax of slicing is

```python
string[start : end : step]

- start : We provide the starting index.
- end : We provide the end index(this is not included in substring).
- step : It is an optional argument that determines the increment between each index for slicing.
```

```python
# declaring the string
str ="100-Days-of-Code-with-Python"

# slicing using indexing sequence
print(str[: 3])
print(str[1 : 5 : 2])
print(str[-1 : -12 : -2])
```

Output:
```python
100
00D
nhyCf-oe
```

#### Reverse a String using Slicing

```python
# declaring the string
str ="100-Days-of-Code-with-Python"

print("Original String :-")
print(str)

# reversing the string using slicing
print("Reverse String :-")
print(str[: : -1])
```

Output:
```python
Original String :-
100-Days-of-Code-with-Python
Reverse String :-
nohtyP-htiw-edoC-fo-syaD-001
```

## Basic String Methods

Python has a set of built-in methods that you can use on strings.


| Function Name | Description                                              |
|---------------|----------------------------------------------------------|
| capitalize()  | Converts the first character to uppercase                |
| casefold()    | Implements caseless string matching                     |
| center()      | Pad the string with the specified character             |
| count()       | Returns the count of occurrences of a substring         |
| encode()      | Encodes the string with the specified encoding scheme  |
| endswith()    | Returns True if the string ends with a given suffix     |
| expandtabs()  | Replace tabs with spaces in the string                  |
| find()        | Returns the lowest index of a substring                 |
| format()      | Formats the string for printing                        |
| format_map()  | Formats a string using values from a dictionary        |
| index()       | Returns the index of the first occurrence of a substring|
| isalnum()     | Checks if all characters are alphanumeric             |
| isalpha()     | Checks if all characters are alphabetic               |
| isdecimal()   | Checks if all characters are decimal                  |
| isdigit()     | Checks if all characters are digits                   |
| isidentifier()| Checks if a string is a valid identifier              |
| islower()     | Checks if all characters are lowercase                |
| isnumeric()   | Checks if all characters are numeric                  |
| isprintable() | Checks if all characters are printable                |
| isspace()     | Checks if all characters are whitespace               |
| istitle()     | Checks if the string is in title case                 |
| isupper()     | Checks if all characters are uppercase                |
| join()        | Concatenates strings with a specified separator       |
| ljust()       | Left-aligns the string within a specified width       |
| lower()       | Converts all characters to lowercase                 |
| lstrip()      | Removes leading characters                            |
| maketrans()   | Creates a translation table                           |
| partition()   | Splits the string at the first occurrence of a separator|
| replace()     | Replaces occurrences of a substring with another     |
| rfind()       | Returns the highest index of a substring             |
| rindex()      | Returns the highest index of a substring             |
| rjust()       | Right-aligns the string within a specified width     |
| rpartition()  | Splits the string into three parts                   |
| rsplit()      | Splits the string from the right by a separator      |
| rstrip()      | Removes trailing characters                          |
| splitlines()  | Splits the string into lines                         |
| startswith()  | Returns True if the string starts with a prefix      |
| strip()       | Removes leading and trailing characters              |
| swapcase()    | Swaps case of characters                             |
| title()       | Converts the string to title case                    |
| translate()   | Modifies the string using translation mappings      |
| upper()       | Converts all characters to uppercase                 |
| zfill()       | Pads the string with zeros on the left               |

Examples of these methods will be covered in the next day lesson.