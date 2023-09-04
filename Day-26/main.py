# Examples of Tuples in Python programming language

# Creating a tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup)
#output: (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Accessing elements of a tuple
print(tup[0])
#output: 1

#Accessing elements of a tuple using negative indexing
print(tup[-1])
#output: 9


mytuple = (1, 2, 3, 4, 5)
 
# tuples are indexed
print(mytuple[1])
print(mytuple[4])
 
# tuples contain duplicate elements
mytuple = (1, 2, 3, 4, 2, 3)
print(mytuple)
 
# adding an element
mytuple[1] = 100
print(mytuple)

#output:
# 2
# 5
# (1, 2, 3, 4, 2, 3)
# Traceback (most recent call last):
#   File "main.py", line 23, in <module>
#     mytuple[1] = 100

var = (1, 2, 3)

print("Value in Var[-1] = ", var[-1])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-3] = ", var[-3])

#output:
# Value in Var[-1] =  3
# Value in Var[-2] =  2
# Value in Var[-3] =  1

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
fruits_tuple = ('apple', 'banana', 'cherry')

# Tuple with mixed data types
mixed_tuple = (1, 'hello', 3.14, True)

# Tuple with a single element (note the trailing comma)
single_element_tuple = (42,)

fruits_tuple = ('apple', 'banana', 'cherry')

# Accessing elements by index
print(fruits_tuple[0])  # Output: 'apple'
print(fruits_tuple[1])  # Output: 'banana'

# Negative indexing
print(fruits_tuple[-1])  # Output: 'cherry'


nested_tuple = ((1, 2), (3, 4), (5, 6))

# Accessing elements of nested tuples
print(nested_tuple[0][0])  # Output: 1
print(nested_tuple[1][1])  # Output: 4
