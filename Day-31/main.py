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

# 5. items() - Returns a list containing a tuple for each key value pair
# Python program to demonstrate working of
# dictionary items()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(text.items())
# Output: dict_items([(1, 'Python'), (2, 'Dictionaries'), (3, 'Methods')])

# 6. keys() - Returns a list containing the dictionary's keys
# Python program to demonstrate working of
# dictionary keys()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(text.keys())
# Output: dict_keys([1, 2, 3])

# 7. pop() - Removes the element with the specified key
# Python program to demonstrate working of
# dictionary pop()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

text.pop(2)
print(text)
# Output: {1: 'Python', 3: 'Methods'}

# 8. popitem() - Removes the last inserted key-value pair
# Python program to demonstrate working of
# dictionary popitem()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

text.popitem()
print(text)
# Output: {1: 'Python', 2: 'Dictionaries'}

# 9. setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# Python program to demonstrate working of
# dictionary setdefault()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(text.setdefault(2))
# Output: Dictionaries

print(text.setdefault(4, "Functions"))
# Output: Functions

print(text)
# Output: {1: 'Python', 2: 'Dictionaries', 3: 'Methods', 4: 'Functions'}

# 10. update() - Updates the dictionary with the specified key-value pairs
# Python program to demonstrate working of
# dictionary update()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

text.update({4: "Functions"})
print(text)
# Output: {1: 'Python', 2: 'Dictionaries', 3: 'Methods', 4: 'Functions'}

# 11. values() - Returns a list of all the values in the dictionary
# Python program to demonstrate working of
# dictionary values()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(text.values())
# Output: dict_values(['Python', 'Dictionaries', 'Methods'])

# 12. del - Deletes the dictionary
# Python program to demonstrate working of
# del
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

del text
print(text)

# Output: NameError: name 'text' is not defined

# 13. len() - Returns the length of the dictionary
# Python program to demonstrate working of
# len()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(len(text))
# Output: 3

# 14. type() - Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type
# Python program to demonstrate working of
# type()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(type(text))
# Output: <class 'dict'>

# 15. cmp() - Compares elements of both dict.
# Python program to demonstrate working of
# cmp()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}
text1 = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(cmp(text, text1))
# Output: 0

# 16. str() - Produces a printable string representation of a dictionary
# Python program to demonstrate working of
# str()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(str(text))
# Output: {1: 'Python', 2: 'Dictionaries', 3: 'Methods'}

# 17. all() - Returns true if all keys of the dictionary are true (or if the dictionary is empty)
# Python program to demonstrate working of
# all()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(all(text))
# Output: True

# 18. any() - Returns true if any key of the dictionary is true. If the dictionary is empty, return false
# Python program to demonstrate working of
# any()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(any(text))
# Output: True

# 19. sorted() - Returns a new sorted list of keys in the dictionary
# Python program to demonstrate working of
# sorted()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(sorted(text))
# Output: [1, 2, 3]

# 20. enumerate() - Returns an enumerate object. It contains the index and value of all the items of dictionary as a pair
# Python program to demonstrate working of
# enumerate()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(list(enumerate(text)))
# Output: [(0, 1), (1, 2), (2, 3)]

# 21. max() - Returns the maximum value among the keys of the dictionary
# Python program to demonstrate working of
# max()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(max(text))
# Output: 3

# 22. min() - Returns the minimum value among the keys of the dictionary
# Python program to demonstrate working of
# min()

text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(min(text))
# Output: 1

# 23. sum() - Returns the sum of all the keys of the dictionary
# Python program to demonstrate working of
# sum()
text = {1: "Python", 2: "Dictionaries", 3: "Methods"}

print(sum(text))
# Output: 6