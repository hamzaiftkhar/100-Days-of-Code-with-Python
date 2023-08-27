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