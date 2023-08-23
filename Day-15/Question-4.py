# Bonus Calculation Program

Year = int(input("Enter the number of years you have worked: "))
Salary = int(input("Enter your salary: "))

if Year <= 1:
    Bonus = Salary * 0.05
elif Year > 1 and Year <= 5:
    Bonus = Salary * 0.15
elif Year > 5 and Year <= 10:
    Bonus = Salary * 0.30
else:
    Bonus = Salary * 0.50

print(f"Your Bonus is: {Bonus}")     