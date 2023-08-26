# Loops in Python - While Loop

## While Loop

- While loop is used to iterate over a block of code as long as the test expression (condition) is true.

- We generally use this loop when we don't know the number of times to iterate beforehand.

- Syntax:

```python
while test_expression:
    Body of while
```

While loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance. 

When a while loop is executed, expr is first evaluated in a Boolean context and if it is true, the loop body is executed. Then the expr is checked again, if it is still true then the body is executed again and this continues until the expression becomes false.

- Example:

```python
# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Python Programming")
```

- Output:

```python
Python Programming
Python Programming
Python Programming
```