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

## Get a list as input from user in Python

In Python, we can use the input() function to take input from the user. Whatever you enter as input, the input function converts it into a string. If you want to convert it into any other data type then you can use the methods like int(), float() or complex().

Getting list as input from user using loop:

```python
# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter the size of List : "))

# iterating till the range
for i in range(0, n):
    element = int(input())
    # adding the element
    lst.append(ele)

print("The input list is : ")
print(lst)
```

Output:

```python
Enter the size of List : 5
1
2
3
4
5
The input list is :
[1, 2, 3, 4, 5]
```

- Time Complexity: O(n), where n is the length of the list 
- Auxiliary Space: O(n) additional space of size n is created where n is the number of elements in the list 