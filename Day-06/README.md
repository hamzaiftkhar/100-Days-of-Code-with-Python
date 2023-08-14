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
