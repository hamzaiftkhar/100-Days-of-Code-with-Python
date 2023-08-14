# How to Take User Input and Type Casting in Python

Developers often have a need to interact with users, either to get data or to provide some sort of result. Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python provides us with two inbuilt functions to read the input from the keyboard. 

- **input ( prompt )**
- **raw_input ( prompt )**

## **input ()**:
 This function first takes the input from the user and converts it into a string. The type of the returned object always will be **<class ‘str’>**. It does not evaluate the expression it just returns the complete statement as String. 

**For example**, Python provides a built-in function called input which takes the input from the user. When the input function is called it stops the program and waits for the user’s input. When the user presses enter, the program resumes and returns what the user typed. 

**Example 1: How input() works in Python?**

```python
# Program to check input
# type in Python

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
```
Output:

```python
Enter number :10
10
Enter name : Hamza
Hamza
```
### How the input function works in Python : 
 
- When **input()** function executes program flow will be stopped until the user has given input.
- The text or message displayed on the output screen to ask a user to enter an input value is optional i.e. the prompt, which will be printed on the screen is optional.
- Whatever you enter as input, the input function converts it into a string. if you enter an integer value still input() function converts it into a string. You need to explicitly convert it into an integer in your code using **typecasting**(Explain below in this article 👇).

## **raw_input()**:
This function works in older version (like Python 2.x). This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store.

**For example**, Python provides a built-in function called raw_input which takes the input from the user. When the raw_input function is called, the program stops and waits for the user to type something. When the user presses Enter, the program resumes and raw_input returns what the user typed as a string.

**Example 2: How raw_input() works in Python?**

```python
# Program to check input
# type in Python

num = raw_input ("Enter number :")
print(num)
name1 = raw_input("Enter name : ")
print(name1)
```
Output:

```python
Enter number :10
10
Enter name : Hamza
Hamza
```
## Typecasting in python
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

### Two Types of Typecasting:
- **Explicit Conversion (Explicit type casting in python)**
- **Implicit Conversion (Implicit type casting in python)**

### Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

#### Example of explicit typecasting:

```python
# Python program to demonstrate explicit type conversion
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
```
Output:

```python
The Sum of both the numbers is:  22
```
### Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type.

 According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

#### Example of implicit typecasting:

```python
# Python program to demonstrate implicit type conversion
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
```
Output:

```python
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```