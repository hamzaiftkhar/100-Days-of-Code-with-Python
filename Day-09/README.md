# Strings in Python

In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

A string is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Strings are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.

Example:

```python
a = "Hamza"
print("Hello " + a)
```
Output:
```python
Hello Hamza
```
Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience
```python
print('He said, "I want to eat an apple"')
```
Output:
```python
He said, "I want to eat an apple"
```

## Multiline Strings

Sometimes, you might need to print a string that spans multiple lines. For example, consider the following string:

You can use three double quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
Or three single quotes:
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

Output:
```python
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```
**Note:** In the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays(Accessing Characters of String)

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Example:
```python
a = "Hello, World!"
print(a[1])
```
Output:
```python
e
```
Example:
```python
name = "Hamza"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
```
Output:
```python
H
a
m
z
a
```

## Looping through String

We can loop through strings using a for loop like this:

```python
for x in "Programming":
  print(x)
```
Output
```python
P
r
o
g
r
a
m
m
i
n
g
```
We will learn about loops in detail in upcoming days. 

## String Length

The **len()** function returns the length of a string:
```python
a = "Hello, World!"
print(len(a))
```
Output:
```python
13
```
## Check String

To check if a certain phrase or character is present in a string, we can use the keyword **in**.

Example:
```python
txt = "The best things in life are free!"
print("free" in txt)
```
Output:
```python
True
```

## Check if NOT in String

To check if a certain phrase or character is NOT present in a string, we can use the keyword **not in**.

Example:
```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```
Output:
```python
True
```
Use it in **if** statement:
```python
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```
Output:
```python
No, 'expensive' is NOT present.
```