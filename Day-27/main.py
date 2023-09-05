# Examples related to topics we have learnt in todays exercise

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1 += tuple2
print(tuple1)  # Output: (1, 2, 3, 4, 5, 6)


original_tuple = (1, 2, 3)
item_to_add = (4,)
new_tuple = original_tuple + item_to_add
print(new_tuple)  # Output: (1, 2, 3, 4)


# Convert tuple to list
original_tuple = (1, 2, 3)
tuple_list = list(original_tuple)

# Add items to the list
tuple_list.append(4)
tuple_list.extend([5, 6])

# Convert the list back to a tuple
new_tuple = tuple(tuple_list)

print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Convert tuple to list
original_tuple = (1, 2, 3)
tuple_list = list(original_tuple)

# Modify items in the list
tuple_list[1] = 10
tuple_list[2] = 20

# Convert the list back to a tuple
new_tuple = tuple(tuple_list)

print(new_tuple)  # Output: (1, 10, 20)


original_tuple = (1, 2, 3, 4, 5)
tuple_list = list(original_tuple)
item_to_remove = 3  # Remove the item with value 3
tuple_list.remove(item_to_remove)
new_tuple = tuple(tuple_list)
print(new_tuple)  # Output: (1, 2, 4, 5)


original_tuple = (1, 2, 3, 4, 5)
item_to_remove = 3
new_tuple = tuple(item for item in original_tuple if item != item_to_remove)
print(new_tuple)  # Output: (1, 2, 4, 5)

#Example 3: Using enumerate for both index and value:
my_tuple = ('apple', 'banana', 'cherry')

for index, value in enumerate(my_tuple):
    print(f"Index {index}: {value}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

#count() method
my_tuple = (1, 2, 2, 3, 4, 2)
count = my_tuple.count(2)
print(count)  # Output: 3

#sorted() method
my_tuple = (3, 1, 2, 5, 4)
sorted_list = sorted(my_tuple)
print(sorted_list)  # Output: [1, 2, 3, 4, 5]

#min() and max() methods
my_tuple = (3, 1, 2, 5, 4)
min_val = min(my_tuple)
max_val = max(my_tuple)
print(min_val)  # Output: 1
print(max_val)  # Output: 5

#len() method
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)  # Output: 5

#sum() method
my_tuple = (1, 2, 3, 4, 5)

total = sum(my_tuple)
print(total)  # Output: 15

#unpacking a tuple
# Creating a tuple
my_tuple = (1, 2, 3)

# Unpacking the tuple
a, b, c = my_tuple

# Printing the unpacked variables
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Unpacking with the * operator
a, b, *rest = my_tuple

# Printing the unpacked variables
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]