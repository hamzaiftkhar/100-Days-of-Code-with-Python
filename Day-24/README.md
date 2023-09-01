# Lists methods in Python Programming

## Python List Slicing

The format for list slicing is of Python List Slicing is as follows:

```
Lst[ Initial : End : IndexJump ]
```

If Lst is a list, then the above expression returns the portion of the list from index Initial to index End, at a step size IndexJump.

List slicing in Python is a common practice and can be used both with positive indexes as well as negative indexes.

```python
# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# Display list
print(Lst[1:5])
```

Output:

```
[70, 30, 20, 90]
```

Example 2:

```python
# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[3:9:2])

# Display sliced list
print(List[::2])

# Display sliced list
print(List[::])
```

Output:

```
Original List:
 [1, 2, 3, 4, 5, 6, 7, 8, 9]

Sliced Lists: 
[4, 6, 8]
[1, 3, 5, 7, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]