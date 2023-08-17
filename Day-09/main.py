# Examples of string

print("A Python course for everyone")

# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Coding
For
Life'''
print("\nCreating a multiline String: ")
print(String1)

#----------------------------------------------

# Python Program to Access
# characters of String

String1 = "100-Days-of-Code"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#----------------------------------------------

#check string using in and not in
String1 = "100-Days-of-Code"
print("Initial String: ")
print(String1)

# Checking if 'Days' is present in
# String or not using in
if 'Days' in String1:
    print("Yes, 'Days' is part of String.")

# Checking if 'Days' is present in
# String or not using in
# with not operator
if 'Days' not in String1: 
    print("Yes, 'Days' is part of String.")
# no output

#----------------------------------------------

# Python Program to
# demonstrate String checking

rollno = "21-abc-123"
print("abc" not in rollno)
print("abc" in rollno)
#----------------------------------------------