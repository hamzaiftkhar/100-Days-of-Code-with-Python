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