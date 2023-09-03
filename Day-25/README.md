# Additional concepts in Lists in Python Programming Language

## List Comprehension

List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list. However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.

Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

### Syntax:

```python
new_list = [expression for_loop_one_or_more conditions]
```

### Examples:

```python
# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(odd_square)
```

Output:

```python
[1, 9, 25, 49, 81]  # using list comprehension
[1, 9, 25, 49, 81]  # without using list comprehension
```