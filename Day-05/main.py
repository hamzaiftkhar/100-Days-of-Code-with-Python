# examples of operators in python

#Input:
x = 5
y = 3
sum = x + y
sub = x - y
mul = x * y
div = x / y
mod = x % y
exp = x ** y
flo = x // y

print ("Sum of x and y is: ", sum)
print ("Subtraction of x and y is: ", sub)
print ("Multiplication of x and y is: ", mul)
print ("Division of x and y is: ", div)
print ("Modulus of x and y is: ", mod)
print ("Exponent of x and y is: ", exp)
print ("Floor division of x and y is: ", flo)

#Output:
#Sum of x and y is:  8
#Subtraction of x and y is:  2
#Multiplication of x and y is:  15
#Division of x and y is:  1.6666666666666667
#Modulus of x and y is:  2
#Exponent of x and y is:  125
#Floor division of x and y is:  1

#----------------------------------------------

ratio = (1+(5**(1/2)))/2
print(ratio)

#Output:
#1.618033988749895

print (((5 + 4) / 3) * 2)

#Output:
#6

quadratic = (3 * (2 ** 2)) - (4 * 2) + 1
print(quadratic)

#Output:
#5

#----------------------------------------------


# Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
import keyword
 
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

#----------------------------------------------

print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

print(True or False)
 
# showing logical operation
# and (returns False)
print(False and True)
 
# showing logical operation
# not (returns False)
print(not True)

#Output:    
#True
#True
#3
#1
#False
#False
#True
#False
#False

#----------------------------------------------

my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete both the variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

#Output:
#20
#GeeksForGeeks
#NameError: name 'my_variable1' is not defined

#----------------------------------------------