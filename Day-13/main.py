a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")



#----------------------------------------------

num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

#----------------------------------------------

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#output: At least one of the conditions is True


# Python program to illustrate short hand if
i = 10
if i < 15: print("i is less than 15")
#output: i is less than 15


# Python program to illustrate short hand if-else
i = 10
print(True) if i < 15 else print(False)
#output: True


# python program to illustrate nested If statement

i = 10
if (i == 10):

	# First if statement
	if (i < 15):
		print("i is smaller than 15")
		
	# Nested - if statement
	# Will only be executed if statement above
	# it is true
	if (i < 12):
		print("i is smaller than 12 too")
	else:
		print("i is greater than 15")
#output: i is smaller than 15


# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)
#output: [16, 9, 15, 18]

num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
#output: Number is Zero.

#----------------------------------------------
# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.

#----------------------------------------------

age = 25
income = 50000

if age >= 18 and income > 30000:
    print("You are eligible for a loan")
else:
    print("You are not eligible for a loan")
#output: You are eligible for a loan

#----------------------------------------------

colors = ["red", "blue", "green"]
if "yellow" in colors:
    print("Yellow is in the list")
else:
    print("Yellow is not in the list")
#output: Yellow is not in the list

#----------------------------------------------