# First Programming Concepts and Arithmetic Operators in Python

## Print() function

The print() function is used to display information on the screen. It is a built-in function in Python.

 We will use this function frequently in this series to check the results of your code. The syntax of the print() function is modeled in the example below:

```python
# Syntax for printing a string of text.

print("Hello folks! its Day-05 of 100DaysOfCode Challenge.")
```
Output:

```python
Hello folks! its Day-05 of 100DaysOfCode Challenge.
```

## Keywords

Keywords are reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language. In Python, keywords are case sensitive.

All the keywords except True, False and None are in lowercase and they must be written as they are. The list of all the keywords is given below.

```python
# List of keywords in Python
Values: True, False, None
Conditions: if, elif, else
Logical operators: and, or, not
Loops: for, in, while, break, continue
Functions: def, return  
```

# Python Keywords

Below is a list of keywords in Python along with their descriptions:

| Keyword    | Description                                      | | Keyword  | Description                                        | | Keyword  | Description                                      |
|------------|--------------------------------------------------|-|----------|----------------------------------------------------|-|----------|--------------------------------------------------|
| and        | Logical Operator                                | | False    | Represents an expression that will result in not being true. | | nonlocal | Non-local variable                            |
| as         | Used to create an alias name                    | | finally  | Used with exceptions                              | | not      | Logical Operator                              |
| assert     | Used for debugging                              | | for      | Used to create a Loop                             | | or       | Logical Operator                              |
| break      | Breaks out of a Loop                            | | from     | Import specific parts of a module                | | pass     | Used when no code execution is desired        |
| class      | Define a class                                  | | global   | Declare a global variable                        | | raise    | Raise exceptions or errors                    |
| continue   | Skip the next iteration of a loop               | | return   | End the execution                                 | | if       | Conditional statement                        |
| def        | Define a Function                               | | import   | Import a module                                   | | del      | Delete an object                              |
| elif       | Conditional statement (else-if)                | | True     | Represents a true expression                      | | try      | Handle errors with try                       |
| else       | Used in a conditional statement               | | is       | Test if two variables are equal                   | | in       | Check if a value is present in a Tuple, List, etc. |
| except     | Handle exceptions                               | | while    | Execute a block of statements in a loop           | | None     | Represents a null value                       |
| lambda     | Create an anonymous function                   | | with     | Used in exception handling                    | | yield    | Create a generator function                   |

### Get the List of all Python keywords
We can also get all the keyword names using the below code.
```python
# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)
```
Output:

```python
[‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘async’, ‘await’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
```

## Arithmetic operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

# Arithmetic Operators in Python

Python can calculate numbers using common mathematical operators, along with some special operators.

Below is a list of arithmetic operators in Python along with their descriptions and syntax:

| Operator | Description                    | Syntax       |
|----------|--------------------------------|--------------|
| +        | Addition: adds two operands     | x + y        |
| -        | Subtraction: subtracts two operands | x - y     |
| *        | Multiplication: multiplies two operands | x * y   |
| /        | Division (float): divides the first operand by the second | x / y |
| //       | Division (floor): divides the first operand by the second, returning an integer quotient | x // y |
| %        | Modulus: returns the remainder when the first operand is divided by the second | x % y |
| **       | Power: Returns first raised to power second | x ** y   |

## Precedence of Arithmetic Operators in Python
The precedence of Arithmetic Operators in python is as follows:

1. **P** – Parentheses
2. **E** – Exponentiation
3. **M** – Multiplication (Multiplication and division have the same precedence)
4. **D** – Division
5. **A** – Addition (Addition and subtraction have the same precedence)
6. **S** – Subtraction

You might find the **PEMDAS** mnemonic device to be helpful in remembering the order.

For all the examples related to above concepts visit [main.py](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/blob/main/Day-05/main.py)