# Examples of Lists in Python in Python Programming

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Printing the entire list
print(numbers)

# Accessing elements in the list
print(numbers[0])  # Prints the first element (1)
print(numbers[2])  # Prints the third element (3)

# Modifying elements in the list
numbers[1] = 10   # Changes the second element to 10
print(numbers)

# Adding elements to the list
numbers.append(6)  # Appends 6 to the end of the list
print(numbers)

# Removing elements from the list
numbers.remove(3)  # Removes the element 3 from the list
print(numbers)

# Finding the length of the list
length = len(numbers)
print("Length of the list:", length)

fruits = ["apple", "banana", "orange", "grape"]
print(fruits)

# Accessing and modifying elements
print(fruits[1])            # Prints "banana"
fruits[2] = "pineapple"     # Changes "orange" to "pineapple"
print(fruits)

# Adding elements
fruits.append("kiwi")       # Appends "kiwi" to the end
print(fruits)

# Removing elements
fruits.remove("apple")      # Removes "apple" from the list
print(fruits)

fruits = ["apple", "banana", "orange", "grape"]

# Accessing elements by index
print(fruits[0])  # Prints "apple"
print(fruits[2])  # Prints "orange"

numbers = [10, 20, 30, 40, 50]

# Accessing elements using negative index
print(numbers[-1])  # Prints the last element (50)
print(numbers[-3])  # Prints the third-to-last element (30)

numbers = [10, 20, 30, 40, 50]

# Checking if an index is within bounds before accessing
index = 3
if index < len(numbers):
    print(numbers[index])
else:
    print("Index out of bounds")

fruits = ["apple", "banana", "orange"]

# Appending a single element
fruits.append("grape")   # Adds "grape" to the end of the list
print(fruits)

# Appending multiple elements
fruits.append("kiwi")
fruits.append("pear")
print(fruits)

numbers = [1, 2, 3, 4, 5]

# Inserting an element at a specific index
numbers.insert(2, 10)   # Inserts 10 at index 2, shifting other elements
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Extending list1 with elements from list2
list1.extend(list2)
print(list1)   # Outputs [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3]

# Using the += operator to append elements
numbers += [4, 5, 6]
print(numbers)   # Outputs [1, 2, 3, 4, 5, 6]

fruits = ["apple", "banana", "orange", "apple", "grape"]

# Removing the first occurrence of a specific value
fruits.remove("apple")
print(fruits)  # Outputs ["banana", "orange", "apple", "grape"]

numbers = [10, 20, 30, 40, 50]

# Removing an element by index
removed_value = numbers.pop(2)  # Removes and returns the value at index 2 (30)
print("Removed:", removed_value)
print(numbers)  # Outputs [10, 20, 40, 50]

numbers = [1, 2, 3, 4, 5]

# Removing the last element using pop()
last_element = numbers.pop()
print("Last Element:", last_element)
print(numbers)  # Outputs [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]

# Clearing the entire list
numbers.clear()
print(numbers)  # Outputs []

numbers = [10, 20, 30, 40, 50]

# Removing an element by index using the del statement
del numbers[2]  # Removes the element at index 2 (30)
print(numbers)  # Outputs [10, 20, 40, 50]

#---------------------------------------------------------------