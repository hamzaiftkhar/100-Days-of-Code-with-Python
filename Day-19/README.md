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