#Examples of Formatting with % Operator.

# Example 1
item = "book"
price = 15.99
formatted_string = "The {} costs ${:.2f}.".format(item, price)
print(formatted_string)
#output: The book costs $15.99.

# Example 2
name = "hasnain"
score = 85
formatted_string = "Hello, %s! Your score is %d." % (name, score)
print(formatted_string)
#output: Hello, hasnain! Your score is 85.

# Example 3
temperature = 25.5
humidity = 70
formatted_string = "Today's temperature is %.1f°C with %d%% humidity." % (temperature, humidity)
print(formatted_string)
#output: Today's temperature is 25.5°C with 70% humidity.

#Examples of Formatting with format() string method.

# Example 1
animal = "dog"
sound = "bark"
formatted_string = "The {} makes a {} sound.".format(animal, sound)
print(formatted_string)
#output: The dog makes a bark sound.

# Example 2
product = "phone"
price = 599.99
formatted_string = "The {} costs ${:.2f}.".format(product, price)
print(formatted_string)
#output: The phone costs $599.99.

# Example 3
course = "Math"
teacher = "Mr. Abid"
formatted_string = "{} class is taught by {}.".format(course, teacher)
print(formatted_string)
#output: Math class is taught by Mr. Abid.

#Examples of Formatting with f-strings.

# Example 1
fruit = "apple"
quantity = 5
formatted_string = f"I have {quantity} {fruit}s."
print(formatted_string)
#output: I have 5 apples.

# Example 2
username = "user.admin"
role = "admin"
formatted_string = f"The user {username} is an {role}."
print(formatted_string)
#output: The user user.admin is an admin.

# Example 3
length = 10
width = 7
area = length * width
formatted_string = f"The area of a rectangle with length {length} and width {width} is {area}."
print(formatted_string)
#output: The area of a rectangle with length 10 and width 7 is 70.

#----------------------------------------------

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#----------------------------------------------

def nametag(first_name, last_name):
    return("{} {}.".format(first_name,last_name[:1]))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

#----------------------------------------------