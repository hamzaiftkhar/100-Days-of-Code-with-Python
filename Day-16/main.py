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

def swap(x, y):
	temp = x
	x = y
	y = temp


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)

# Output:
# 2
# 3

#------------------------------------------------------------

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

calculateGmean(4, 6)

# Output:
# 2.4

#------------------------------------------------------------

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# Output:
# 99 100

#------------------------------------------------------------

def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)
#output will print to the screen

#------------------------------------------------------------

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(my_trip_km*2))

# Output:
# The distance in kilometers is 88.0

#------------------------------------------------------------