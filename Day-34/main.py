# Examples of Exception Handling in Python

# Example 1
try:
    print(1/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
# Output: You cannot divide by zero!

# Example 2
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
# Output: division by zero

# Example 3
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
except:
    print("Something went wrong!")
# Output: division by zero


try:
    # Code that may raise exceptions
    value = int("abc")  # This will raise a ValueError
    result = 10 / 0      # This will raise a ZeroDivisionError
except ValueError as ve:
    print("ValueError occurred:", ve)
except ZeroDivisionError as zde:
    print("ZeroDivisionError occurred:", zde)
# Output: ValueError occurred: invalid literal for int() with base 10: 'abc'


try:
    # Code that may raise an exception
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("An error occurred:", e)
finally:
    print("This will always execute, regardless of exceptions.")
# Output: An error occurred: division by zero

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print("An error occurred:", e)
# Output: An error occurred: Division by zero is not allowed


try:
    value = int(input("Enter an integer: "))
except ValueError as ve:
    print("ValueError occurred:", ve)
else:
    print("You entered:", value)
# Output: Enter an integer: 10


try:
    age = int(input("Enter your age: "))
except ValueError as ve:
    print("Invalid input. Please enter a valid age.")
else:
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
# Output: Enter your age: 20
#         You are eligible to vote.


file = None
try:
    file = open("example.txt", "r")
    # Perform operations on the file
except FileNotFoundError as fnf:
    print("File not found:", fnf)
except Exception as e:
    print("An error occurred:", e)
finally:
    if file:
        file.close()
# Output: File not found: [Errno 2] No such file or directory: 'example.txt'


try:
    num = int(input("Enter a number: "))
except ValueError as ve:
    print("Invalid input. Please enter a valid number.")
else:
    result = num * 2
    print("Double of the number:", result)
finally:
    print("This block always executes, whether there was an exception or not.")
# Output: Enter a number: 10
#         Double of the number: 20
#         This block always executes, whether there was an exception or not.



import sqlite3

conn = None
try:
    conn = sqlite3.connect("my_database.db")
    # Perform database operations
except sqlite3.Error as sqle:
    print("Database error:", sqle)
finally:
    if conn:
        conn.close()



try:
    with open("data.txt", "r") as file:
        data = file.read()
except FileNotFoundError as fnf:
    print("File not found:", fnf)
else:
    print("File read successfully:", data)
# Output: File not found: [Errno 2] No such file or directory: 'data.txt'