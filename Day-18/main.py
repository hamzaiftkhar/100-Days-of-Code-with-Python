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

import random

target_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess < target_number:
        print("Too low! Try again.")
        continue
    elif guess > target_number:
        print("Too high! Try again.")
        continue
    else:
        print("Congratulations! You guessed the number.")
        break

#In this example, the loop prompts the user to guess a random number between 1 and 100. If the guess is too low, the loop continues and asks for another guess. If the guess is too high, the loop continues and asks for another guess. If the guess is correct, the loop breaks and displays a congratulatory message.

num = 1

while num <= 10:
    if num % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(num)
    num += 1

# In this example, the loop prints odd numbers from 1 to 10 while skipping even numbers using the pass statement. The pass statement is a null operation that does nothing. It is used as a placeholder when a statement is required syntactically, but no code needs to be executed.

while True:
    user_input = input("Enter a positive integer (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a positive integer.")
        continue
    
    number = int(user_input)
    
    if number % 2 == 0:
        print("Even number detected. Skipping.")
        pass
    else:
        print("Odd number detected.")
    
    print(f"Number squared: {number ** 2}")

# In this example, the loop prompts the user to enter a positive integer. If the input is not a valid positive integer, the loop continues and asks for input again. If the input is valid, the loop checks if the number is even. If the number is even, the loop skips the rest of the code and asks for input again. If the number is odd, the loop prints a message and displays the square of the number. If the user enters 'exit', the loop breaks and displays a message.

num = int(input("Enter a positive integer: "))
factorial = 1
counter = num

while counter > 0:
    factorial *= counter
    counter -= 1
else:
    print(f"The factorial of {num} is {factorial}.")

# In this example, the loop calculates the factorial of a positive integer. The loop starts with the value of the integer and multiplies it by the value of the counter. The counter is decremented by 1 in each iteration. The loop continues until the counter reaches 0. When the counter reaches 0, the loop breaks and displays the factorial of the integer.

total = 0
sentinel = -1  # Sentinel value to end the loop

print("Enter numbers to sum. Enter -1 to finish.")

while True:
    num = int(input("Enter a number: "))
    
    if num == sentinel:
        break  # Exit the loop when sentinel value is entered
    
    total += num

print(f"The sum of the numbers is: {total}")

# In this example, the loop prompts the user to enter numbers to sum. The loop continues until the user enters the sentinel value (-1). When the sentinel value is entered, the loop breaks and displays the sum of the numbers.

row = 1

while row <= 5:
    column = 1
    
    while column <= 10:
        product = row * column
        print(f"{row} * {column} = {product}")
        column += 1
        
    row += 1
    print("------------------")

# In this example, the loop prints the multiplication table from 1 to 5. The outer loop iterates over the rows and the inner loop iterates over the columns. The inner loop prints the product of the row and column. The outer loop increments the row by 1 and prints a separator after each row.

while True:
    # Code to be executed at least once
    
    user_input = input("Do you want to continue? (y/n): ")
    
    if user_input.lower() != 'y':
        break

# In this example, the loop prompts the user to continue. The loop continues until the user enters 'n'. The loop executes at least once because the condition is checked at the end of the loop.