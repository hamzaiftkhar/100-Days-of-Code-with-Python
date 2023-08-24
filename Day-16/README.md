# Functions in Python

Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Some Benefits of Using Functions :

- Increase Code Reusability
- Increase Code Readability

### Python Function Declaration

In Python, we declare a function using the def keyword. After the keyword, we specify the name of the function along with parentheses. The code block within every function starts with a colon (:) and is indented.

```python
def function_name():
    # code block
```

## Types of Functions

There are two types of functions in Python:

- Built-in Functions
- User-defined Functions

### 1. Built-in Functions

Python has several built-in functions. These functions are already defined in Python libraries and can be used directly by the user.
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), abs(), all() etc.

Example:

```python
# Python program to illustrate
# built-in functions

# abs() : Returns the absolute value of a number
print(abs(-1))

# all() : Returns True if all elements of the iterable are true (or if the iterable is empty).
print(all([1, 2, 3, 4, 5]))
```

Output:

```python

1   # abs() : Returns the absolute value of a number
True    # all() : Returns True if all elements of the iterable are true (or if the iterable is empty).
```

### 2. User-defined Functions

User-defined functions are the functions that are defined by the user at the time of writing the program. The user can give any name to his/her function. The user-defined functions are created to perform a specific task. The user-defined functions are reusable and can be called through the program any number of times.

Syntax:

```python
def function_name(parameters):
    # code block


Rules: -

- Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
- Any parameters and arguments should be placed within the parentheses.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

```

#### Terms: -

- **return value** - the value or variable returned as the end result of a function

- **parameter (argument)** -  a value passed into a function for use within the function

- **refactoring code** - a process to restructure code without changing functionality.

- **function definition** - the code that makes up a function

- **function call** - the code used to pass control to a function; also the name given to the function

- **function** - a named set of instructions that defines a set of actions in Python

- **function header** - the first line of a function definition

- **function body** - the code inside a function definition

Example:

```python
# Python program to illustrate
# user-defined functions

def name(first_name, last_name):
    print("Hello,", first_name, last_name)

name("Python", "Programmer")
```

Output:

```python
Hello, Python Programmer
```

## Calling a  Python Function

Once we have defined a function, we can call it from anywhere in our program. To call a function, we simply need to write the function name with the parentheses.

Example:

```python
# Python program to illustrate
# calling a function

# A simple Python function
def fun():
    print("Welcome to 100-days-of-code-with-python-programming")


# Driver code to call a function
fun()
```

Output:

```python
Welcome to 100-days-of-code-with-python-programming
```

## Python Function with Parameters

In Python, we can pass a variable number of arguments to a function. This means that we do not need to know the exact number of arguments that we will pass to a function beforehand. We can call a function with any number of arguments.

Syntax:

```python
 def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
```

Example:

```python
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
```

Output:

```python
The addition of 5 and 15 results 20.
```

## Python Function Arguments

In Python, we can pass a variable number of arguments to a function. This means that we do not need to know the exact number of arguments that we will pass to a function beforehand. We can call a function with any number of arguments.

Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

In this example, we will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.

Example:

```python
# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)
```

Output:

```python
even   # evenOdd(2) : even
odd    # evenOdd(3) : odd
```