a = complex(8, 2)
b = True
c = "Hamza"
d = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Output:
# <class 'complex'>
# <class 'bool'>
# <class 'str'>
# <class 'NoneType'>

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Hamza", "age":20, "canVote":True}
print(dict1)

# Output:
# [8, 2.3, [-4, 5], ['apple', 'banana']]
# (('parrot', 'sparrow'), ('Lion', 'Tiger'))
# {'name': 'Hamza', 'age': 20, 'canVote': True}

#----------------------------------------------

# float to int
a = 10.5
b = int(a)
print(b)
#output: 10

# int to str
a = 10
b = str(a)
print(b)
#output: 10

# str to int
a = "10"
b = int(a)
print(b)
#output: 10

#----------------------------------------------

#Example 1

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

# Output:
# Each person needs to pay: 27.2

#----------------------------------------------

#Example 2

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "ABC"
middle_name = "LMN"
last_name = "XYZ"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation , first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

# Output:
# Dr. ABC LMN XYZ, Ph.D.
# Dr. ABC LMN XYZ , Ph.D.

#----------------------------------------------

#Example 3

print("5 * 3 = " + str(5*3)) 
 
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string. 

# Output:
# 5 * 3 = 15

#----------------------------------------------

