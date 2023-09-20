# Local and Global Variables in python

- Python Global variables are those which are not defined inside any function and have a global scope.
- Python local variables are those which are defined inside a function and their scope is limited to that function only. 

In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function.

## Python Local Variables

"Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function."

### Creating a Local Variable

To create a local variable in Python, we simply need to assign a value to a variable inside a function. We can do this by using the assignment operator (=).

```python
def func():
    x = 7
    print(x)

func()
```

Output:

```python
7
```

**Q. Can a Local Variable be accessed outside the function?**

Ans. No, a local variable cannot be accessed outside the function. If we try to access a local variable outside the function, it will give an error.

```python
def func():
    x = 7
    print(x)

func()
print(x)
```

Output:

```python
7
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    print(x)
NameError: name 'x' is not defined
```