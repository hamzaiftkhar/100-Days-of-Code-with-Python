# Introduction to Lists in Python Programming

## What is a List?

A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

Lists are great to use when you want to work with many related values. They enable you to keep data together that belongs together, condense your code, and perform the same methods and operations on multiple values at once.

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

Syntax
```python
list_name = [item_1, item_2, item_3]
```

## Creating a List

Lists are created using square brackets [ ] with commas separating items.

The list contains different data types like integer, float, string, etc.

```python
# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)
```

Output
```python
[]
[1, 2, 3]
[1, 'Hello', 3.4]
```

- Time Complexity: **O(1).**
- Space Complexity: **O(n).**

## Accessing Elements in a List

There are various ways in which we can access the elements of a list.

In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing.

- **Positive Indexing:** Starts from 0 from the left side of the list.

```python
# Python program to demonstrate
# accessing of element from list

# Creating a List with
# the use of multiple values
List = ["100-Days", "of", "Code"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])
```

Output
```python
Accessing a element from the list    
100-Days    #print(List[0])
Code        #print(List[2])
```

- **Negative Indexing:** In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

```python
List = [1, 2, '100-Days', 4, 'of', 6, 'Code']

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])
```

Output

```python
Accessing element using negative indexing
Code    #print(List[-1])
of      #print(List[-3])
```

Complexities for Accessing elements in a Lists:

- Time Complexity: **O(1).**
- Space Complexity: **O(1).**

## Getting the size of Python list

To get the size of a Python list, we can use the built-in function len(). It returns the number of elements in a list.

```python
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))
```

Output

```python
0
3
```

## Adding Elements to a Python List

Elements can be added to the List by using the built-in append() function. Only one element at a time can be added to the list by using the append() method, for the addition of multiple elements with the append() method, loops are used. Tuples can also be added to the list with the use of the append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of the append() method.

```python
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
```

Output

```python
Initial blank List: 
[]
List after Addition of Three elements: 
[1, 2, 4]

List after Addition of elements from 1-3: 
[1, 2, 4, 1, 2, 3]
```

Complexities for Adding elements in a Lists(append() method):

- Time Complexity: **O(1).**
- Space Complexity: **O(1).**

### Method 2: Using insert() method

append() method only works for the addition of elements at the end of the List, for the addition of elements at the desired position, insert() method is used. Unlike append() which takes only one argument, the insert() method requires two arguments(position, value). 

```python
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Python')
print("\nList after performing Insert Operation: ")
print(List)
```

Output

```python
Initial List: 
[1, 2, 3, 4]

List after performing Insert Operation: 
['Python', 1, 2, 3, 12, 4]
```

Complexities for Adding elements in a Lists(insert() method):

- Time Complexity: **O(n).**
- Space Complexity: **O(1).**

### Method 3: Using extend() method

Other than append() and insert() methods, there’s one more method for the Addition of elements, extend(), this method is used to add multiple elements at the same time at the end of the list.

Note – append() and extend() methods can only add elements at the end.

```python
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Python', 'Programming'])
print("\nList after performing Extend Operation: ")
print(List)
```

Output

```python
Initial List: 
[1, 2, 3, 4]

List after performing Extend Operation: 
[1, 2, 3, 4, 8, 'Python', 'Programming']
```

Complexities for Adding elements in a Lists(extend() method):

- Time Complexity: **O(n).**
- Space Complexity: **O(1).**

## Removing Elements from the List

### Method 1: Using remove() method

Elements can be removed from the List by using the built-in remove() function but an Error arises if the element doesn’t exist in the list. Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The remove() method removes the specified item.

**Note:** Remove method in List will only remove the first occurrence of the searched element.

```python
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
```

Output

```python
Initial List: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

List after Removal of two elements: 
[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]
```

Complexities for Deleting elements in a Lists(remove() method):

- Time Complexity: **O(n).**
- Space Complexity: **O(1)**

### Method 2: Using pop() method

pop() function can also be used to remove and return an element from the list, but by default it removes only the last element of the list, to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.

```python
List = [1, 2, 3, 4, 5]
 
# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)
 
# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
```

Output

```
List after popping an element: 
[1, 2, 3, 4]

List after popping a specific element: 
[1, 2, 4]
```