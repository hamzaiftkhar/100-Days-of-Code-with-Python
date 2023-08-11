# Our First Program, Comments, Escape sequence and print in Python

## Our First Program

```python
print("Hello World!")
```
output:
```python   
Hello World!
```
now we have idea what is Python Programming Language, Here is the most basic examples and dive deeper into what's going on. When we run this code either locally on our machine or on a web interpreter, the words hello world appear on the screen just like shown above.

### print() function

"The print function is a built-in function in Python. It prints the given object to the standard output device (screen) or to the text stream file. It is used to print the message in the double-quotes("") to the console. "

```python
print (5 + 5)
```
Output:
```python
10
```
 The print function is part of the basic Python language, whenever we use keywords or functions that are part of the language, we're using the programming language's syntax to tell the computer what to do.

## Comments in Python

Comments are lines that exist in computer programs that are ignored by compilers and interpreters. Including comments in programs makes code more readable for humans as it provides some information or explanation about what each part of a program is doing.

- #### Single Line Comments

In Python, we use the hash (#) symbol to start writing a comment.

```python
#This is a comment
print("Our First Program")
```
Output:
```python
Our First Program
```
- #### Multi Line Comments

We can have comments that extend up to multiple lines. One way is to use the hash(#) symbol at the beginning of each line. For example:

```python
#This is a long comment
#and it extends
#to multiple lines
print("We are learning comments")
```
Output:
```python
We are learning comments
```
Another way of doing this is to use triple quotes, either ''' or """.

These triple quotes are generally used for multi-line strings. But they can be used as multi-line comment as well. Unless they are not docstrings, they do not generate any extra code.

```python
"""This is also a
perfect example of
multi-line comments"""
print("Examples of multi-line comments")
```
Output:
```python
Examples of multi-line comments
```
## Escape Sequence

To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

```python
print("This is a "double quoted" string.")
```
Output:
```python
SyntaxError: invalid syntax
```
To fix this error, we can use the escape sequence character \":

```python
print("This is a \"double quoted\" string.")
```
Output:
```python
This is a "double quoted" string.
```
Here are some other escape sequence characters:

| Escape Sequence | Meaning |
| --- | --- |
| \\\\ | Backslash (\) |
| \\' | Single quote (') |
| \\" | Double quote (") |
| \\n | Newline |
| \\t | Tab |
| \\b | Backspace |
| \\r | Carriage return |

All of these concepts are important to understand as we continue to learn more about Python. We'll be using them in our code and it's important to understand what they mean.