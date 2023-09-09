# Examples of Python Dictionary methods 

# Dictionary Methods

# 1. clear() - Removes all the elements from the dictionary
# Python program to demonstrate working of
# dictionary clear()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

text.clear()
print('text =', text)
# Output: text = {}


# 2. copy() - Returns a shallow copy of the dictionary
# Python program to demonstrate working of
# dictionary copy()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

text1 = text.copy()
print('text1 =', text1)
# Output: text1 = {1: 'Python', 2: 'Dictionaries', 3: 'Methods'}

# 3. fromkeys() - Returns a dictionary with the specified keys and value
# Python program to demonstrate working of
# dictionary fromkeys()
text = ('Python', 'Dictionaries', 'Methods')
text1 = dict.fromkeys(text)
print(text1)
# Output: {'Python': None, 'Dictionaries': None, 'Methods': None}

text1 = dict.fromkeys(text, 10)
print(text1)
# Output: {'Python': 10, 'Dictionaries': 10, 'Methods': 10}

# 4. get() - Returns the value of the specified key
# Python program to demonstrate working of
# dictionary get()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(text.get(2))
# Output: Dictionaries
