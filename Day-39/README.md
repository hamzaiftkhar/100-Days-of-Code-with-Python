# How Import works in Python

Import in python is similar to #include header_file in C/C++. Python modules can get access to code from another module by importing the file/function using import.
Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

```python
import math
```

This statement creates a new namespace containing all of the functions and variables defined in the math module. You can then access these functions and variables using the dot operator. For example, to access the pi variable defined in the math module, you would use the following statement:

```python
math.pi
```

This statement returns the value of pi, which is 3.141592653589793.

Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

```python
import math

result = math.sqrt(9)
print(result)  # Output: 3.0
```

In this example, we import the math module and then use the sqrt function to calculate the square root of 9. The result is then printed to the console.

## Importing a Module Using "as" Keyword

You can also import a module using **as** keyword. For example, to import the math module using the keyword as, you would use the following statement:

```python
import math as m
```

here m is the alias of math module. Now you can access the math module using m instead of math. For example, to access the square root function defined in the math module, you would use the following statement:

```python
import math as m

result = m.sqrt(9)
print(result)  # Output: 3.0

print(m.pi)  # Output: 3.141592653589793
```

Output:

```python
3.0
3.141592653589793
```

## Importing Specific Functions from a Module

You can also import specific functions from a module using the from keyword. For example, to import the sqrt function from the math module, you would use the following statement:

```python
from math import sqrt
```

This statement imports the sqrt function from the math module. Now you can use the sqrt function without using the dot notation. For example, to calculate the square root of 9, you would use the following statement:

```python
from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0
```

In this example, we import the sqrt function from the math module and then use it to calculate the square root of 9. The result is then printed to the console.

we can also import multiple functions from a module using the from keyword. For example, to import the sqrt and pi functions from the math module, you would use the following statement:

```python
from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```

In this example, we import the sqrt and pi functions from the math module and then use them to calculate the square root of 9 and print the value of pi. The result is then printed to the console.

## Importing All Functions from a Module

You can also import all functions from a module using the * operator. For example, to import all functions from the math module, you would use the following statement:

```python
from math import *
```

This statement imports all functions from the math module. Now you can use all functions from the math module without using the dot notation. For example, to calculate the square root of 9, you would use the following statement:

```python
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```

Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.