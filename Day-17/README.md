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