#Task-01 Calculator that perform all the basic operations to two numbers entered by the user.

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

ans1 = a+b
ans2=a-b
ans3=a*b
ans4=a/b
ans5 = a//b
ans6 = a**b
ans7 = a%b

print("\nAddition of a and b is ", ans1)
print("\nsubtraction of a and b is ", ans2)
print("\nMultiplication of a and b is ", ans3)
print("\nDivision of a and b is ", ans4)
print("\nFloor division of a and b is ", ans5)
print("\na exponent b is ", ans6)
print("\na modulus of b is ", ans7)
