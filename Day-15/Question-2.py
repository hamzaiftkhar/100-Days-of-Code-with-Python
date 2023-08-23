# Program to check weather the input number is 4 digit number or not

num = input("Enter a Number: ")

if len(num) == 4:
    print("The number is a 4 digit number")
elif len(num) > 4:
    print("The number is greater than 4 digit number")
else:
    print("The number is less than 4 digit number")

