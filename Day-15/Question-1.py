# Program To Check Weather The Last Digit Of a Number is Divisible by 3 or Not

# Taking Input From User
number = int(input("Enter a Number: "))

# Checking Condition
if number % 10 == 0 or number % 10 == 3 or number % 10 == 6 or number % 10 == 9:
    print("Last Digit of Number is Divisible by 3")
else:
    print("Last Digit of Number is Not Divisible by 3")

# Alternate Method

num = input("Enter a Number: ")
if int(num[-1]) % 3 == 0:
    print("Last Digit of Number is Divisible by 3")
else:
    print("Last Digit of Number is Not Divisible by 3")

# Alternate Method

num = input("Enter a Number: ")

if num[-1] in ["0", "3", "6", "9"]:
    print("Last Digit of Number is Divisible by 3")
else:
    print("Last Digit of Number is Not Divisible by 3")
    