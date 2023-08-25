# Examples of Arguments of functions

# Example 1
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Hamza")                # Output: Hello, Hamza!
greet("Ali", message="Hi")    # Output: Hi, Ali!

# Example 2
def power(base, exponent=2):
    return base ** exponent

result1 = power(3)     # 3^2 = 9
result2 = power(2, 4)  # 2^4 = 16

# Example 3
def generate_email(username, domain="example.com"):
    return f"{username}@{domain}"

email1 = generate_email("Python")                  # Python@example.com
email2 = generate_email("Programming", domain="xyz.com")  # Programming@xyz.com

#--------------------------------------------------------------

# Example 1
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(name="hamza", age=20)
#Output: hamza is 20 years old.

# Example 2
def create_order(product, quantity, discount=0):
    total_price = quantity * product.price * (1 - discount)
    print(f"Total price: ${total_price:.2f}")

create_order(product=my_product, quantity=5, discount=0.1)
# Output: Total price: $45.00

# Example 3
def print_info(first_name, last_name, **info):
    print(f"Name: {first_name} {last_name}")
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(first_name="ABC", last_name="DEF", age=30, city="PAKISTAN")
# Output:
# Name: ABC DEF
# age: 30
# city: PAKISTAN

#--------------------------------------------------------------

# Example 1
def add(a, b):
    return a + b

result = add(3, 5)  # Output: 8

# Example 2
def calculate_total(price, tax_rate):
    total_price = price * (1 + tax_rate)
    return total_price

total_cost = calculate_total(100, 0.1)  # $100 + 10% tax

# Example 3
def create_sentence(subject, verb, object):
    return f"{subject} {verb} {object}."

sentence = create_sentence("Cats", "are", "adorable")
# Output: Cats are adorable.

#--------------------------------------------------------------
# (A bit Complex Examples of Arguments of functions, it will be easy to understand after concepts of loops)

# Example 1
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)       # Output: 1, 2, 3

# Example 2
def process_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

process_data(name="Alice", age=25, location="London")
# Output:
# name: Alice
# age: 25
# location: London


# Example 3
def display_items(prefix, *items, suffix="end"):
    print(prefix)
    for item in items:
        print(f"- {item}")
    print(suffix)

display_items("Start:", "Apple", "Banana", "Orange", suffix="Finish:")
# Output:
# Start:
# - Apple
# - Banana
# - Orange
# Finish:

#--------------------------------------------------------------

"""
Best Practices
Assign the default value as none and then check in the function if the expected list or dictionary argument is none or not.

If it is none then assign it with a list or dictionary depending on your requirement."""

# using None as values of the default arguments

print('#list')
def appendItem(itemName, itemList=None):
	if itemList == None:
		itemList = []
	itemList.append(itemName)
	return itemList


print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))


# using None as value of default parameter

print('\n\n#dictionary')
def addItemToDictionary(itemName, quantity, itemList = None):
	if itemList == None:
		itemList = {}
	itemList[itemName] = quantity
	return itemList


print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))

"""
#list
['notebook']
['pencil']
['eraser']

#dictionary
{'notebook': 4}
{'pencil': 1}
{'eraser': 1}

Here you can clearly see that every time a function is called and a list or dictionary is not passed as an argument to the function then it creates a new list or dictionary.

"""

#--------------------------------------------------------------

def square(number):
    return number ** 2

result = square(5)
print(result)  # Output: 25

#--------------------------------------------------------------
def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

quot, rem = divide_and_remainder(17, 5)
print("Quotient:", quot)     # Output: Quotient: 3
print("Remainder:", rem)     # Output: Remainder: 2

#--------------------------------------------------------------

def create_greeting(name):
    def get_greeting():
        return "Hello"
    return f"{get_greeting()}, {name}!"

message = create_greeting("World")
print(message)  # Output: Hello, World!

#--------------------------------------------------------------

def get_person_info(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }

person_data = get_person_info("Bob", 30, "New York")
print(person_data["name"])  # Output: Bob
print(person_data["age"])   # Output: 30

#--------------------------------------------------------------

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(7))   # Output: False
print(is_even(10))  # Output: True

#--------------------------------------------------------------

def print_and_return(value):
    print("Value:", value)
    return None

result = print_and_return(42)
print(result)  # Output: Value: 42 \n None

#--------------------------------------------------------------

# Python program to illustrate functions
# can return another function

def create_adder(x):
	def adder(y):
		return x + y

	return adder

add_15 = create_adder(15)

print("The result is", add_15(10))

# Returning different function
def outer(x):
	return x * 10

def my_func():
	
	# returning different function
	return outer

# storing the function in res
res = my_func()

print("\nThe result is:", res(10))

#Output:
#The result is 25

#The result is: 100

#--------------------------------------------------------------