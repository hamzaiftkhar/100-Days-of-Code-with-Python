# TASK 02 Solution BMI CALCULATOR 

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

print("\nBody Mass Index according to your height and weight is : ", str(bmi))

#Conditional statements to check BMI and print the result (future concepts)

# if bmi < 18.5:
#     print("\nYou are underweight")
# elif bmi < 25:
#     print("\nYou have a normal weight")
# elif bmi < 30:
#     print("\nYou are slightly overweight")
# elif bmi < 35:
#     print("\nYou are obese")
# else:
#     print("\nYou are clinically obese")