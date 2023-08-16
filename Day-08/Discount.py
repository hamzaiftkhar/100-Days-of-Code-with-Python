# Task-03 It Calculates the amount of discount given to a customer

# Input
price = float(input("Enter the price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Process
discount_amount = price * discount / 100
final_price = price - discount_amount

# Output
print("The discount amount is: ", discount_amount)
print("The final price is: ", final_price)