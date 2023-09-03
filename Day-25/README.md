# Additional concepts in Lists in Python Programming Language

## List Comprehension

List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list. However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.

Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

### Syntax

```python
new_list = [expression for_loop_one_or_more conditions]
```

### Examples

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

### Getting list as input from user using list comprehension

```python
# For list of integers
lst1 = []

# For list of strings/chars
lst2 = []

lst1 = [int(item) for item in input("Enter the list items : ").split()]

lst2 = [item for item in input("Enter the list items : ").split()]

print(lst1)
print(lst2)
```

Output:

```python
Enter the list items : 1 2 3 4 5
Enter the list items : a b c d e
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd', 'e']
```

### Getting list as input from user using exception handling

```python
# try block to handle the exception
try:
    my_list = []

    while True:
        my_list.append(int(input()))

# if the input is not-integer, just print the list
except:
    print(my_list)
```

Output:

```python
1
2
3
4
5
a    #Non-integer input exception occur here
[1, 2, 3, 4, 5]
```

**Note**: For more concept about Exception Handling in Python, review our Exception Handling lecture.

## List Sorting in Python

- #### Sort list Alphanumerically

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

Output:

```python
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

- #### Sort List in Descending Order

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```

Output:

```python
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

- #### Case Insensitive Sort

By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```

Output:

```python
['Kiwi', 'Orange', 'banana', 'cherry']
```

**If you want a case-insensitive sort function, use str.lower as a key function:**

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```

Output:

```python
['banana', 'cherry', 'Kiwi', 'Orange']
```