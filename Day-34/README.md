# Exception Handling in Python

Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which change the normal flow of the program. 

## Different types of exceptions in python

In Python, there are several built-in exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

- **SyntaxError:** This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
- **TypeError:** This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
- **NameError:** This exception is raised when a variable or function name is not found in the current scope.
- **IndexError:** This exception is raised when an index is out of range for a list, tuple, or other sequence types.
- **KeyError:** This exception is raised when a key is not found in a dictionary.
- **ValueError:** This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
- **AttributeError:** This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
- **IOError:** This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
- **ZeroDivisionError:** This exception is raised when an attempt is made to divide a number by zero.
- **ImportError:** This exception is raised when an import statement fails to find or load a module.

These are just a few examples of the many types of exceptions that can occur in Python. It’s important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing.

## Difference between Syntax Error and Exception

Syntax errors occur when the parser detects an incorrect statement. Observe the following example:

```python
# Syntax Error
if a < 3
    print(a)
```

The above code will give the following error:

```python
  File "<ipython-input-1-8b1a6e5c4c2b>", line 2
    if a < 3
            ^

SyntaxError: invalid syntax
```

As you can see, the parser detected the error and raised a SyntaxError before executing the code. This is because the parser cannot understand the statement if it is not syntactically correct.

- On the other hand, exceptions occur when syntactically correct Python code results in an error. Observe the following example:

```python
# Exception
a = 1
b = "2"
c = a + b
```

The above code will give the following error:

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-8b1a6e5c4c2b> in <module>
      2 a = 1
      3 b = "2"
----> 4 c = a + b

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

As you can see, the code is syntactically correct, but the addition operation is not supported between an integer and a string. This results in a TypeError exception.

## Try and Except Statement – Catching Exceptions

The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.

The syntax of the try-except block is:

```python
try:
    # Code that can raise an exception
except:
    # Code that executes if an exception is raised in the try block
```

The try block must be followed by an except statement at the very least. You can also add an else clause after the except clause, which will execute if no exceptions are raised in the try block.

```python
try:
    # Code that can raise an exception
except:
    # Code that executes if an exception is raised in the try block
else:
    # Code that executes if no exceptions are raised in the try block
```

You can also add a finally clause after the except or else clauses, which will execute regardless of whether an exception is raised or not.

```python
try:
    # Code that can raise an exception
except:
    # Code that executes if an exception is raised in the try block
else:
    # Code that executes if no exceptions are raised in the try block
finally:
    # Code that executes regardless of whether an exception is raised or not
```

Example :

```python
# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))

    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))

except:
    print ("An error occurred")
```

Output :

```python
Second element = 2

An error occurred
```