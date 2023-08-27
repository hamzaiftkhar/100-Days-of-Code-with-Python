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