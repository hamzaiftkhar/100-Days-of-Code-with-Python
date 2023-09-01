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
```

## List Methods in Python

Python List Methods has multiple methods to work with Python lists, Below we’ve explained all the methods you can use with Python lists, for example, append(), copy(), insert(), and more.

| S.no | Method   | Description                                         |
| ---- | -------- | --------------------------------------------------- |
| 1    | `append()`   | Used for appending and adding elements to the end of the List. |
| 2    | `copy()`     | It returns a shallow copy of a list. |
| 3    | `clear()`    | This method is used for removing all items from the list. |
| 4    | `count()`    | Counts the elements. |
| 5    | `extend()`   | Adds each element of the iterable to the end of the List. |
| 6    | `index()`    | Returns the lowest index where the element appears. |
| 7    | `insert()`   | Inserts a given element at a given index in a list. |
| 8    | `pop()`      | Removes and returns the last value from the List or the given index value. |
| 9    | `remove()`   | Removes a given object from the List. |
| 10   | `reverse()`  | Reverses objects of the List in place. |
| 11   | `sort()`     | Sorts a List in ascending, descending, or user-defined order. |
| 12   | `min()`      | Calculates the minimum of all the elements of the List. |
| 13   | `max()`      | Calculates the maximum of all the elements of the List. |