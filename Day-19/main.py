# Examples of for loop in python

fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange
# grape
#---------------------------------------------

numbers = [2, 5, 8, 10]
sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)

# Output:
# Sum: 25
#---------------------------------------------

word = "Python"
for char in word:
    print(char)

# Output: it will print each character in new line
#---------------------------------------------

for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10
#---------------------------------------------

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
#---------------------------------------------

numbers = [2, 4, 6, 8, 10, 12]
for num in numbers:
    if num > 8:
        break
    print(num)

# Output:
# 2
# 4
# 6
# 8
#---------------------------------------------

numbers = [1, 3, 5, 7, 9, 11]
for num in numbers:
    if num % 3 == 0:
        continue
    print(num)

# Output:
# 1
# 5
# 7
# 11
#---------------------------------------------

fruits = ["apple", "banana", "orange", "grape"]
search_fruit = "kiwi"
for fruit in fruits:
    if fruit == search_fruit:
        print("Found", search_fruit)
        break
else:
    print(search_fruit, "not found in the list")

# Output:
# kiwi not found in the list
#---------------------------------------------

numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 == 1:
        print("Not all numbers are even")
        break
else:
    print("All numbers are even")

# Output:
# All numbers are even
#---------------------------------------------

numbers = [1, 4, 7, 9, 10, 12]
for num in numbers:
    if num % 2 == 0:
        print("Found an even number:", num)
        continue
    if num > 9:
        print("Encountered a number greater than 9, stopping loop")
        break

# Output:
# Found an even number: 4
# Found an even number: 10
# Encountered a number greater than 9, stopping loop
#---------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 22 years old

#---------------------------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
cities = ["New York", "San Francisco", "Los Angeles"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

#---------------------------------------------

sum_even = 0
for i in range(0, 11, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)

# Output:
# Sum of even numbers: 30
#---------------------------------------------

numbers = [2, 4, 6, 8, 10]
search_number = 7

for num in numbers:
    if num == search_number:
        print(f"Found {search_number} in the list")
        break
else:
    print(f"{search_number} not found in the list")

# Output:
# 7 not found in the list
#---------------------------------------------

"""
Printing range with Python Continue Statement
Consider the situation when you need to write a program that prints the number from 1 to 10, but not 6. 

It is specified that you have to do this using a loop and only one loop is allowed to use. Here comes the usage of the continue statement. What we can do here is we can run a loop from 1 to 10 and every time we have to compare the value of the loop variable with 6. If it is equal to 6 we will use the continue statement to continue to the next iteration without printing anything, otherwise, we will print the value."""

# loop from 1 to 10
for i in range(1, 11):

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")

# Output:
# 1 2 3 4 5 7 8 9 10
#---------------------------------------------