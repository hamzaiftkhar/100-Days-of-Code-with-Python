# Conditional Statements (if-elif-else) in Python

## What is Conditional Statements?

Conditional statements are used to perform different actions based on different conditions.

Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

- if
- if-else
- if-else-elif
- nested if-else-elif.

1. ## if statement

   The if statement is used to check a condition. If the condition is true, a block of code (if-block) will be executed. If the condition is false, the if-block will be skipped and the next block of code (if any) will be executed.

   Syntax:

   ```python
   if condition:
       statement(s)
   ```

   Example:

   ```python
   a = 33
   b = 200
   if b > a:
      print("b is greater than a")
    ```

    Output:

    ```python
    b is greater than a
    ```

    **Note** : Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

    ```python
    applePrice = 210
    budget = 200
    if (applePrice <= budget):
        print("Usman, add 1 kg Apples to the cart.")
    else:
        print("Usman, do not add Apples to the cart.")
    ```

    Output:

    ```python
    Usman, do not add Apples to the cart.
    ```

    As we know, python uses indentation to identify a block. So the block under an if statement will be identified as shown in the below example:

     ```python
    if condition:
       statement1
    statement2

    # Here if the condition is true, if block 
    # will consider only statement1 to be inside 
    # its block.
    # However, statement2 will be executed
    ```