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
PYTHON IS AWESOME

Converted String:
python is awesome

Converted String:
Python Is Awesome

Converted String:
pYTHON IS AWESOME

Converted String:
Python is awesome

Original String
Python is awesome
```