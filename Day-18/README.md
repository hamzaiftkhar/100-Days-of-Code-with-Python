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

## While Loop with Control Statement

Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.

### Continue Statement

- It returns the control to the beginning of the loop.

Example:

```python
# Prints all letters except 'P' and 'o'
i = 0
a = 'Python Program'

while i < len(a):
    if a[i] == 'P' or a[i] == 'o':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1
```

- Output:

```python
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : n
Current Letter :
Current Letter : r
Current Letter : a
Current Letter : g
Current Letter : r
Current Letter : a
Current Letter : m
```

### Break Statement

- It brings control out of the loop.

Example:

```python
# Prints all letters except 't' and 'o'
i = 0
a = 'Python Program'

while i < len(a):
    if a[i] == 't' or a[i] == 'o':
        i += 1
        break

    print('Current Letter :', a[i])
    i += 1
```

- Output:

```python
Current Letter : P
Current Letter : y
```

### Pass Statement

- We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.

Example:

```python
# An empty loop
a = 'Python Programming'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)
```

- Output:

```python
Value of i : 18
```