# Typecasting Examples

# Python program to demonstrate
# implicit type Casting

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts
# b to float
b = 3.0
print(type(b))

# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

# Python automatically converts
# e to float as it is a float division
e = b / a
print(e)
print(type(e))

# Python program to demonstrate
# type Casting

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))

a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)

# User Input Examples

username = input("Enter username:")
print("Username is: " + username)

#----------------------------------------------

# Taking input as string
color = input("What color is rose?: ")
print(color)

# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)

# Taking input as float
# Typecasting to float
price = float(input("Price of each rose?: "))
print(price)

# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

# using eval() to evaluate data type of user input
num = eval(input('Enter a number: '))
print('You Entered:', num)

print('Data type of num:', type(num))

#----------------------------------------------

a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)

print(int(x) + int(y))
