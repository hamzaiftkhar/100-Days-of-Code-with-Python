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