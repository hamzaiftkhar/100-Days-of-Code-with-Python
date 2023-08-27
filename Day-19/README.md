# FOR Loops in Python Programming

## What is FOR Loop?

A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

## Syntax

```python
for val in sequence:
    Body of for

for x in range(1, 11):
    print(x)    
```

Here, **val** is the variable that takes the value of the item inside the sequence on each iteration.

Loop continues until we reach the last item in the sequence.

The body of for loop is separated from the rest of the code using indentation.

range() function is used to generate a sequence of numbers. It returns a range object.

### Example: Python for Loop

```python
for x in "banana":
  print(x)

```

### Output

```python
b
a
n
a
n
a
```

The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.

Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. A for loop works well when you want to iterate over a sequence of elements.

## The range() Function

We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.

Syntax of range()

```python
range(start, stop, step_size)

- start: Starting number of the sequence.
- stop: Generate numbers up to, but not including this number.
- step_size: Difference between each number in the sequence.
```

### Example: Python range() function

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))
```

### Output

```python
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]
```

We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.

### Example: Python range() function in for loop

```python
for k in range(4,9):
    print(k)
```

### Output

```python
4
5
6
7
8
```

## For loop control statements

Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.

### 1. Continue Statement

It returns the control to the beginning of the loop.

```python
for val in sequence:
    if condition:
        continue
    Body of for
```

#### Example: Python continue statement

```python
for val in "Python":
    if val == "i":
        continue
    print(val)
```

Output

```python
P
y
t
h
o
n
```

### 2. Break Statement

It brings control out of the loop.

```python
for val in sequence:
    if condition:
        break
    Body of for
```

#### Example: Python break statement

```python
for letter in 'Python':     # First Example

    # break the loop as soon it sees 't'
    # or 't'
    if letter == 'h' or letter == 't':
        break

print('Current Letter :', letter)
```

Output

```python
Current Letter : t
```

### 3. Pass Statement

We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.

```python
for val in sequence:
    pass
```

#### Example: Python pass statement

```python

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
```

Output

```python
#all characters will be pass and no output will be generated
```

## Else with Python For Loop

Python supports having an else statement associated with a loop statement.

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20.

#### Example: Python else statement with for loop

```python
# Python program to demonstrate
# for-else loop

for i in range(1, 4):
    print(i)
else: # Executed because no break in for
    print("No Break\n")
```

Output

```python
1
2
3
No Break
```

## Python For Loop with Zip()

This code uses the zip() function to iterate over two lists (fruits and colors) in parallel. The for loop assigns the corresponding elements of both lists to the variables fruit and color in each iteration. Inside the loop, the print() function is used to display the message “is” between the fruit and color values. The output will display each fruit from the list of fruits along with its corresponding color from the colours list.

#### Example: Python for loop with zip()

```python
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]

for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)
```

Output

```python
apple is red
banana is yellow
cherry is green
```

## Nested for loop in Python

In Python, we can have a for loop inside another for loop. This is called nested for loop.

In nested for loop, for loop is placed inside the body of another for loop.

```python
for val in sequence:
    for val in sequence:
        Body of inner for
    Body of outer for
```

#### Example: Python nested for loop

```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
```

Output

```python
1
2 2
3 3 3
4 4 4 4
```