# Examples of Functions in Python 

string = "Hello, world!"
length = len(string)
print(length)  # Output: 13

num = -5
absolute_value = abs(num)
print(absolute_value)  # Output: 5


numbers = [7, 2, 9, 4, 1, 6]
maximum = max(numbers)
minimum = min(numbers)
print(maximum)  # Output: 9
print(minimum)  # Output: 1

#------------------------------------------------------------

def calculate_rectangle_area(length, width):
    area = length * width
    return area

result = calculate_rectangle_area(5, 3)  # Calling the function with arguments 5 and 3
print(result)  # Output: 15


#------------------------------------------------------------
def add(a, b):
    sum_result = a + b
    return sum_result

result = add(7, 8)
print(result)  # Output: 15

total = add(3, 4)
print("The total is:", total)  # Output: The total is: 7

#------------------------------------------------------------

def reverse_string(input_str):
    return input_str[::-1]

result = reverse_string("Python")
print(result)  # Output: nohtyP

#------------------------------------------------------------

def calculate_list_sum(numbers):
    total = sum(numbers)
    return total

numbers = [2, 4, 6, 8, 10]
result = calculate_list_sum(numbers)
print(result)  # Output: 30

#------------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = 30
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(fahrenheit_temp)  # Output: 86.0

#------------------------------------------------------------

