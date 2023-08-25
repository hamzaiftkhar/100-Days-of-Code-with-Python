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
