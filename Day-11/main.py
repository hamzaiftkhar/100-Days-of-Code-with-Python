# Examples of python String methods 

#capitalize() - Converts the first character to upper case
print("capitalize() - Converts the first character to upper case")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
print()

#casefold() - Converts string into lower case
print("casefold() - Converts string into lower case")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
print()
#output: hello, and welcome to my world!


#center() - Returns a centered string
print("center() - Returns a centered string")
txt = "banana"
x = txt.center(20)
print(x)
print()
#output:       banana

#count() - Returns the number of times a specified value occurs in a string
print("count() - Returns the number of times a specified value occurs in a string")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
print()
#output: 2  (apple occurs 2 times in the string)

#encode() - Returns an encoded version of the string
print("encode() - Returns an encoded version of the string")
txt = "My name is Ståle"
x = txt.encode()
print(x)
print()
#output: b'My name is St\xc3\xa5le'

#endswith() - Returns true if the string ends with the specified value
print("endswith() - Returns true if the string ends with the specified value")
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
print()
#output: True

#expandtabs() - Sets the tab size of the string
print("expandtabs() - Sets the tab size of the string")
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print()
#output: H e l l o

#find() - Searches the string for a specified value and returns the position of where it was found
print("find() - Searches the string for a specified value and returns the position of where it was found")
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
print()
#output: 7

#format() - Formats specified values in a string
print("format() - Formats specified values in a string")
txt = "For only {price:.2f} dollars!"   
print(txt.format(price = 49))
print()
#output: For only 49.00 dollars!

#index() - Searches the string for a specified value and returns the position of where it was found
print("index() - Searches the string for a specified value and returns the position of where it was found")
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
print()
#output: 7

#isalnum() - Returns True if all characters in the string are alphanumeric
print("isalnum() - Returns True if all characters in the string are alphanumeric")
txt = "Company12"
x = txt.isalnum()
print(x)
print()
#output: True

#isalpha() - Returns True if all characters in the string are in the alphabet
print("isalpha() - Returns True if all characters in the string are in the alphabet")
txt = "CompanyX"
x = txt.isalpha()
print(x)
print()
#output: True

#isdecimal() - Returns True if all characters in the string are decimals
print("isdecimal() - Returns True if all characters in the string are decimals")
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)
print()
#output: True

#isdigit() - Returns True if all characters in the string are digits
print("isdigit() - Returns True if all characters in the string are digits")
txt = "50800"
x = txt.isdigit()
print(x)
print()
#output: True

#isidentifier() - Returns True if the string is an identifier
print("isidentifier() - Returns True if the string is an identifier")
txt = "Demo"
x = txt.isidentifier()
print(x)
print()
#output: True

#islower() - Returns True if all characters in the string are lower case
print("islower() - Returns True if all characters in the string are lower case")
txt = "hello world!"
x = txt.islower()
print(x)
print()
#output: True

#isnumeric() - Returns True if all characters in the string are numeric
print("isnumeric() - Returns True if all characters in the string are numeric")
txt = "565543"
x = txt.isnumeric()
print(x)
print()
#output: True

#isprintable() - Returns True if all characters in the string are printable
print("isprintable() - Returns True if all characters in the string are printable")
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
print()
#output: True

#isspace() - Returns True if all characters in the string are whitespaces
print("isspace() - Returns True if all characters in the string are whitespaces")
txt = "   "
x = txt.isspace()
print(x)
print()
#output: True

#istitle() - Returns True if the string follows the rules of a title
print("istitle() - Returns True if the string follows the rules of a title")
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
print()
#output: True

#isupper() - Returns True if all characters in the string are upper case
print("isupper() - Returns True if all characters in the string are upper case")
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
print()
#output: True

#join() - Joins the elements of an iterable to the end of the string
print("join() - Joins the elements of an iterable to the end of the string")
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print()
#output: John#Peter#Vicky

#ljust() - Returns a left justified version of the string
print("ljust() - Returns a left justified version of the string")
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
print()
#output: banana               is my favorite fruit.

#lower() - Converts a string into lower case
print("lower() - Converts a string into lower case")
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
print()
#output: hello my friends

#lstrip() - Returns a left trim version of the string
print("lstrip() - Returns a left trim version of the string")
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
print()
#output: of all fruits banana      is my favorite

#maketrans() - Returns a translation table to be used in translations
print("maketrans() - Returns a translation table to be used in translations")
txt = "Hello Hamza!"
mytable = txt.maketrans("H", "J")
print(txt.translate(mytable))
print()
#output: Jello Jamza!

#partition() - Returns a tuple where the string is parted into three parts
print("partition() - Returns a tuple where the string is parted into three parts")
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print()
#output: ('I could eat ', 'bananas', ' all day')

#replace() - Returns a string where a specified value is replaced with a specified value
print("replace() - Returns a string where a specified value is replaced with a specified value")
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
print()
#output: I like apples

#rfind() - Searches the string for a specified value and returns the last position of where it was found
print("rfind() - Searches the string for a specified value and returns the last position of where it was found")
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
print()
#output: 12

#rindex() - Searches the string for a specified value and returns the last position of where it was found
print("rindex() - Searches the string for a specified value and returns the last position of where it was found")
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
print()
#output: 12

#rjust() - Returns a right justified version of the string
print("rjust() - Returns a right justified version of the string")
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
print()
#output:              banana is my favorite fruit.

#rpartition() - Returns a tuple where the string is parted into three parts
print("rpartition() - Returns a tuple where the string is parted into three parts")
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print()
#output: ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

#rsplit() - Splits the string at the specified separator, and returns a list
print("rsplit() - Splits the string at the specified separator, and returns a list")
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
print()
#output: ['apple', 'banana', 'cherry']

#rstrip() - Returns a right trim version of the string
print("rstrip() - Returns a right trim version of the string")
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
print()
#output: of all fruits      banana is my favorite

#split() - Splits the string at the specified separator, and returns a list
print("split() - Splits the string at the specified separator, and returns a list")
txt = "welcome to the Python world."
x = txt.split()
print(x)
print()
#output: ['welcome', 'to', 'the', 'Python', 'world.']

#splitlines() - Splits the string at line breaks and returns a list
print("splitlines() - Splits the string at line breaks and returns a list")
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
print()
#output: ['Thank you for the music', 'Welcome to the jungle']

#startswith() - Returns true if the string starts with the specified value
print("startswith() - Returns true if the string starts with the specified value")
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
print()
#output: True

#strip() - Returns a trimmed version of the string
print("strip() - Returns a trimmed version of the string")
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
print()
#output: of all fruits banana is my favorite

#swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("swapcase() - Swaps cases, lower case becomes upper case and vice versa")
txt = "Hello My Name Is HAMZA"
x = txt.swapcase()
print(x)
print()
#output: hELLO mY nAME iS hamza

#title() - Converts the first character of each word to upper case
print("title() - Converts the first character of each word to upper case")
txt = "Welcome to my world"
x = txt.title()
print(x)
print()
#output: Welcome To My World

#translate() - Returns a translated string
print("translate() - Returns a translated string")
txt = "Hello Hamza!"
mytable = txt.maketrans("H", "J")
print(txt.translate(mytable))
print()
#output: Jello Jamza!

#upper() - Converts a string into upper case
print("upper() - Converts a string into upper case")
txt = "Hello my friends"
x = txt.upper()
print(x)
print()
#output: HELLO MY FRIENDS

#zfill() - Fills the string with a specified number of 0 values at the beginning
print("zfill() - Fills the string with a specified number of 0 values at the beginning")
txt = "50"
x = txt.zfill(10)
print(x)
print()
#output: 0000000050

#format_map() - Formats specified values in a string
print("format_map() - Formats specified values in a string")
txt = "For only {price:.2f} dollars!"
print(txt.format_map({'price': 49}))
print()
#output: For only 49.00 dollars!
