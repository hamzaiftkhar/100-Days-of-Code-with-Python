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

