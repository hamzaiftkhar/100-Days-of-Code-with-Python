# Decorators in Python Programming

## What are Decorators?

Decorators are functions that take another function as an argument, add some functionality to it and return another function without altering the source code of the original function.

Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

The basic syntax for using a decorator is the following:

```python
@decorator
def function():
    pass
```

The decorator is placed above the function definition and is prefixed with the @ symbol. The decorator can be any callable object that takes a function as an argument and returns a new function.

## How decorators work?

As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

```python
@decorator
def hello_decorator():
    print("Python")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = decorator(hello_decorator)''`
```

**Example: Decorators without function arguments**

```python
def greet(fx):
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

hello()
```

**Output:**

```python
Good Morning
Hello world
Thanks for using this function
```