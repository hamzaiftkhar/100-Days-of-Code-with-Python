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

2. ## if-else Statements

    The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with if statement to execute a block of code when the if condition is false. 

    Syntax:

    ```python
    if (condition):
        # Executes this block if
        # condition is true
    else:
        # Executes this block if
        # condition is false
    ```

    Example:

    ```python
    # python program to illustrate If else statement
    #!/usr/bin/python

    i = 20
    if (i < 15):
        print("i is smaller than 15")
        print("i'm in if Block")
    else:
        print("i is greater than 15")
        print("i'm in else Block")
    print("i'm not in if and not in else Block")
    ```

    Output:

    ```python
    i is greater than 15
    i'm in else Block
    i'm not in if and not in else Block
    ```

    - Example of Python if else statement in a list

    ```python
     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_odd_labels = [
        "even"
        if num % 2 == 0
        else "odd"
        for num in numbers
    ]

    print(even_odd_labels)
    ```

    Output:

    ```python
    ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
    ```

3. ## if-elif-else Statements

    Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

    Here, a user can decide among multiple options. The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final else statement will be executed.

    Syntax:

    ```python
    if (condition):
        # Executes this block if
        # condition1 is true
    elif (condition2):
        # Executes this block if
        # condition2 is true
    elif (condition3):
        # Executes this block if
        # condition3 is true
    else:
        # Executes this block if
        # none of the above condition is true
    ```

    Example:

    ```python
    # Python program to illustrate if-elif-else ladder
    #!/usr/bin/python

    i = 20
    if (i == 10):
        print("i is 10")
    elif (i == 15):
        print("i is 15")
    elif (i == 20):
        print("i is 20")
    else:
        print("i is not present")
    ```

    Output:

    ```python
    i is 20
    ```

    - Example of Python if elif else statement in a list

    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_odd_labels = [
        if num % 2 == 0:
            print("even")
        elif num % 2 != 0:
            print("odd")
        else:
            print("unknown")
        for num in numbers
    ]
    ```

    Output:

    ```python
    odd      #1
    even     #2
    odd      #3
    even     #4
    odd      #5
    even     #6
    odd      #7
    even     #8
    odd      #9
    even    #10
    ```