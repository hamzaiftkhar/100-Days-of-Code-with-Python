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

## While Loop with Else

As discussed above, while loop executes the block until a condition is satisfied. When the condition becomes false, the statement immediately after the loop is executed. The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed.

**Note:** The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

Example:

```python
# Python program to demonstrate
# while-else loop

i = 0
while i < 4:
    i += 1
    print(i)
else: # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else: # Not executed as there is a break
    print("No Break")
```

- Output:

```python
1
2
3
4
No Break

1
```

## Nested While Loop

- We can have a while loop inside another while loop. This is called nested while loop.

Example:

```python
# Python program to illustrate
# nested while loops

i = 1

while i <= 3:
    print("While Loop", end=' ')
    j = 1
    while j <= 3:
        print("Nested While Loop", end=' ')
        j = j + 1
    i = i + 1
    print()
```

- Output:

```python
While Loop Nested While Loop Nested While Loop Nested While Loop
While Loop Nested While Loop Nested While Loop Nested While Loop
While Loop Nested While Loop Nested While Loop Nested While Loop
```

## Sentinel Controlled While Loop

- Sentinel controlled while loop is used when we don't know the number of times to iterate beforehand but know the sentinel value which signifies the end of loop.

Example:

```python
# Python program to illustrate
# sentinel controlled while loop

a = int(input('Enter a number (-1 to quit): '))

while a != -1:
    a = int(input('Enter a number (-1 to quit): '))

```

- Output:

```python
Enter a number (-1 to quit): 1
Enter a number (-1 to quit): 2
Enter a number (-1 to quit): 3
Enter a number (-1 to quit): 4
Enter a number (-1 to quit): 5
Enter a number (-1 to quit): -1
```

#### Explanation:

- First, it asks the user to input a number. if the user enters -1 then the loop will not execute
- User enter 6 and the body of the loop executes and again ask for input
- Here user can input many times until he enters -1 to stop the loop
- User can decide how many times he wants to enter input.

## How to emulate do while loop in python?

- Python doesn’t have do-while loop. But we can emulate this behavior using while loop.

- To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

- The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

```python
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
```

- Output:

```python
Enter a positive number: 1
1
Enter a positive number: 2
2
Enter a positive number: 3
3
Enter a positive number: -4
-4
```