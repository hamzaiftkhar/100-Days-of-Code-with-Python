# Program to Calculate electricity bill

unit = int(input("Enter the number of units consumed: "))

if unit <= 100:
    price_per_unit = 10
elif unit > 100 and unit <= 200:
    price_per_unit = 18   
elif unit > 200 and unit <= 300:
    price_per_unit = 25
else:
    price_per_unit = 30

basic_amount = unit * price_per_unit
fuel_chargers = basic_amount * 0.20
government_tax = basic_amount * 0.25
service_chargers = basic_amount * 0.10

total_bill = basic_amount + fuel_chargers + government_tax + service_chargers

total = round(total_bill, 2)

print(f"Total Bill: {total}")