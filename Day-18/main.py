# examples of while loops

i = 1
while i < 6:
  print(i)
  i += 1

#Output:
# 1
# 2
# 3
# 4
# 5

num = 1
while num <= 10:
    if num % 2 == 1:  # Skip odd numbers
        num += 1
        continue
    print(num)
    num += 1

# In this example, the loop prints even numbers from 1 to 10 while skipping odd numbers using the continue statement.


countdown = 10
while countdown > 0:
    if countdown % 2 == 0:  # Skip even numbers
        countdown -= 1
        continue
    print(countdown)
    countdown -= 1

# In this example, the loop prints odd numbers from 9 to 1 while skipping even numbers using the continue statement.


while True:
    user_input = input("Enter a positive number: ")
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a positive number.")
        continue
    
    number = int(user_input)
    if number <= 0:
        print("Invalid input. Please enter a positive number.")
        continue
    
    print(f"Your input: {number}")
    break

#In this example, the loop prompts the user to enter a positive number. If the input is not a valid positive number, the loop continues and asks for input again. If the input is valid, the loop breaks and displays the entered number.