# Function Arguments and Return Statements

Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

In this example, we will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.

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
even   # 2 is even
odd    # 3 is odd
```

## Types of Python Function Arguments

There are four types of arguments that can be passed to a function in Python:

1. Default argument
2. Keyword arguments (named arguments)
3. Positional arguments
4. Arbitrary arguments (variable-length arguments *args and **kwargs)

### 1. Default Arguments

Default arguments are those arguments that take default values if no argument value is passed during the function call. The default value is assigned by using the assignment (=) operator of the form keyword argument = value.

Let’s understand this through a function student. The function student contains 3-arguments out of which 2 arguments are assigned with default values. So, the function student accepts one required argument (firstname), and rest two arguments are optional. 

```python
def student(firstname, lastname ='End', standard ='Fifth'):

    print(firstname, lastname, 'studies in', standard, 'Standard')
```

In the above function, firstname is a required argument, and lastname and standard are optional arguments. If we call the function with only one argument, it will use the default value for the remaining arguments.

```python
def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 positional argument
student('John')

# 3 positional arguments
student('John', 'Gates', 'Seventh')

# 2 positional arguments
student('John', 'Gates')
student('John', 'Seventh')
```

Output:

```python
John Mark studies in Fifth Standard      # 1 positional argument
John Gates studies in Seventh Standard   # 3 positional arguments
John Gates studies in Fifth Standard     # 2 positional arguments
John Seventh studies in Fifth Standard   # 2 positional arguments
```

We need to keep the following points in mind while calling functions: 

- In the case of passing the keyword arguments, the order of arguments is important.
- There should be only one value for one parameter.
- The passed keyword name should match with the actual keyword name.
- In the case of calling a function containing non-keyword arguments, the order is important.

### 2. Keyword Arguments

Keyword arguments are those arguments that are passed by using the name (keyword) so that the values are assigned to the respective parameters. The order of the arguments doesn’t matter here.

The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

```python
def name(first_name, middle_name, last_name):
    print("Hello,", first_name, middle_name, last_name)

name(middle_name = "Python", last_name = "Programming", first_name = "World")
```

Output:

```python
Hello, World Python Programming
```

Calling functions with keyword arguments is useful when the function has a lot of optional arguments. It helps in avoiding confusion as to which argument is being passed and what value is being assigned to which parameter.

```python
def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Semester')

# 1 keyword argument
student(firstname ='Hamza')

# 2 keyword arguments
student(firstname ='Hamza', standard ='Seventh')

# 2 keyword arguments
student(lastname ='Iftikhar', firstname ='Hamza')
```

Output:

```python
Hamza Mark studies in Fifth Semester  # 1 keyword argument
Hamza Mark studies in Seventh Semester  # 2 keyword arguments
Hamza Iftikhar studies in Fifth Semester  # 2 keyword arguments
```

### 3. Positional Arguments

Positional arguments are those arguments that are passed to the function in the same order as they are received. The order of the arguments is crucial here.

Position-only arguments mean whenever we pass the arguments in the order we have defined function parameters in which if you change the argument position then you may get the unexpected output. We should use positional Arguments whenever we know the order of argument to be passed. So now, we will call the function by using the position-only arguments in two ways and In both cases, we will be getting different outputs from which one will be correct and another one will be incorrect.

```python
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because argument is given in order
print("Case-1:")
nameAge("Python", 20)
# You will get incorrect output because argument is not in order
print("\nCase-2:")
nameAge(20, "Python")
```

Output:

```python
Case-1:      # Correct Output
Hi, I am Python
My age is  20

Case-2:      # Incorrect Output
Hi, I am 20
My age is  Python
```

**Note:** We should use the positional argument if we know the order of arguments or before using read the function you use and know the order of arguments to be passed over there otherwise you can get the wrong output as you can see in above-explained example for positional Argument.

### 4. Arbitrary Arguments

Arbitrary arguments are those arguments that are accepted by the function but are not defined. It means that a function can be called with any number of arguments.

There are two types of arbitrary arguments:

- Non-Keyword Variable-length arguments (*args)
- Keyword variable-length arguments (**kwargs)

#### Variable-length arguments (*args)

Variable-length arguments are those arguments that are passed to the function with an asterisk (*). The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as the parameter excluding asterisk (*).

```python
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', '100-Days-of-Code-with-Python')
```

Output:

```python
Hello
Welcome
to
100-Days-of-Code-with-Python
```

#### Keyword variable-length arguments (**kwargs)

Keyword variable-length arguments are those arguments that are passed to the function with a double asterisk ** preceding the parameter name. The arguments are passed as a dictionary and these arguments make a dictionary inside the function with name same as the parameter excluding double asterisk **.

```python
# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='100', mid='Days-of', last='Python Programming')
```

Output:

```python
first == 100
mid == Days-of
last == Python Programming
```