# Examples of list Comprehension

# Example 1
# Create a list of squares from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 2
# Create a list of even numbers from 1 to 10
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

# Example 3
# Create a list of odd numbers from 1 to 10
odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
print(odd_numbers)
# Output: [1, 3, 5, 7, 9]

# Example 4
# Create a list of common numbers from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_numbers = [i for i in list1 if i in list2]
print(common_numbers)
# Output: [3, 4, 5]

# Example 5
names = ["Ahsan", "Sarah", "hamza", "Usman", "Ali", "Omar"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
# Output: ['Ahsan', 'Sarah', 'hamza', 'Usman']

# Example 6
string = "Hello, World!"
uppercase_chars = [char.upper() for char in string if char.isalpha()]
# Result: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

# Example 7
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 8
words = ["apple", "banana", "cherry", "date", "elderberry"]
vowel_words = [word for word in words if word[0].lower() in 'aeiou']
# Result: ['apple']

# Example 9
# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())
	# adding the element
	lst.append(ele)

print(lst)

# Example 10
# try block to handle the exception
try:
	my_list = []

	while True:
		my_list.append(int(input()))

# if the input is not-integer, just print the list
except:
	print(my_list)

# Example 11
# For list of integers
lst1 = []

# For list of strings/chars
lst2 = []

lst1 = [int(item) for item in input("Enter \
				the list items : ").split()]

lst2 = [item for item in input("Enter \
				the list items : ").split()]

print(lst1)
print(lst2)

# Example 12
numbers = [4, 2, 8, 1, 6]
descending_numbers = sorted(numbers, reverse=True)
print(descending_numbers)  # Result: [8, 6, 4, 2, 1]

# Example 13
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
original_list.sort()
print(original_list)  # Result: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Example 14
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(original_list)
print(sorted_list)  # Result: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Example 15
fruits = ["banana", "apple", "cherry", "date", "elderberry"]

# Sort the list in ascending order
ascending_order = sorted(fruits)
print("Ascending Order:", ascending_order)

# Sort the list in descending order
descending_order = sorted(fruits, reverse=True)
print("Descending Order:", descending_order)