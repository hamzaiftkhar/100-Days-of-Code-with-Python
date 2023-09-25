# read, readlines and other file methods

## Read a file line by line using readline() method

**readlines()** is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines. We can iterate over the list and strip the newline ‘\n’ character using strip() function.

Example:

```python
# Python code to
# demonstrate readlines()

L = ["Python\n", "for\n", "Fun\n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
```

Output:

```python
Line1: Python
Line2: for
Line3: Fun
```

## Read a file line by line using read() method

**read()** is used to read all the content of a file at once. It returns the content as a single string, and if the size hint is specified, returns exactly that number of characters.

Example:

```python
# Python code to
# demonstrate read()

L = ["Python\n", "for\n", "Fun\n"]

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.read()

print(Lines)
```

Output:

```python
Python
for
Fun
```

## Read a file line by line using for loop and list comprehension

**for loop** is used to iterate over a file object. It returns the content of a file as a string. We can use strip() function to remove the newline character from the end of the line.

Example:

```python
with open('myfile.txt') as f:
    lines = [line for line in f]

print(lines)

# removing the new line characters
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)
```

Output:

```python
['Python\n', 'for\n', 'Fun\n']
['Python', 'for', 'Fun']
```
