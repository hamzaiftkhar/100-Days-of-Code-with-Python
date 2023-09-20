# Examples of Local and Global Variables

# Local Variable

def myfunc():
    x = 300
    print(x)

myfunc()

# Example 1: Local variable within a function
def example_function():
    name = "Alice"  # name is a local variable
    print("Hello, " + name)

example_function()  # Calling the function

# Example 2: Local variable within a loop
for i in range(5):
    count = i  # count is a local variable within the loop
    print("Iteration:", count)

# Example 3: Local variable in a conditional statement
def check_age(age):
    if age >= 18:
        status = "Adult"  # status is a local variable
    else:
        status = "Minor"  # status is a different local variable
    print("Age status:", status)

check_age(22)
check_age(15)


# Global Variable

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Python"
f()
print(s)


# This function uses global variable s
def f():
	s += 'Programming'
	print("Inside Function", s)


# Global scope
s = "I love Python"
f()


# This function modifies the global variable 's'
def f():
	global s
	s += ' Programming'
	print(s)
	s = "Look for Python Developer"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)


## Examples printing both local and global Variables

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
