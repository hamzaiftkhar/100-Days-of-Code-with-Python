# Basic and Advance String Methods in Python

**Python string** is a sequence of Unicode characters that is enclosed in quotation marks. In this article, we will discuss the in-built function i.e. the functions provided by Python to operate on strings.

**Note:** Every string method does not change the original string instead returns a new string with the changed attributes. 

### Case Changing of Strings

The below functions are used to change the case of the strings.

- lower(): Converts all uppercase characters in a string into lowercase
- upper(): Converts all lowercase characters in a string into uppercase
- title(): Convert string to title case
- swapcase(): Swap the cases of all characters in a string
- capitalize(): Convert the first character of a string to uppercase.

```python
# Python3 program to show the
# working of upper() function
text = 'Python is awesome'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())

#swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)
```

Output:

```python
Converted String:
PYTHON IS AWESOME   #upper

Converted String:
python is awesome   #lower

Converted String:
Python Is Awesome   #title

Converted String:
pYTHON IS AWESOME   #swapcase

Converted String:
Python is awesome   #capitalize

Original String
Python is awesome   #original
```


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