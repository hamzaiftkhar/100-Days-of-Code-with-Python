# Examples of dictionaries in Python

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Dictionary with multiple data types
mixed_dict = {
    "name": "Genius",
    "age": 25,
    "is_student": True,
    "grades": [90, 85, 88]
}


# Nested Dictionaries

employees = {
    "emp1": {
        "name": "Ali",
        "age": 35
    },
    "emp2": {
        "name": "Ahmed",
        "age": 28
    }
}

# Accessing items in a dictionary

print(thisdict["brand"])
#output: Ford

print(thisdict.get("model"))
#output: Mustang

# Changing values in a dictionary

thisdict["year"] = 2018
print(thisdict)

#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Looping through a dictionary

for key in thisdict:
    print(key)

#output: brand
#        model
#        year

for key in thisdict:
    print(thisdict[key])

#output: Ford
#        Mustang
#        2018

for key, value in thisdict.items():
    print(key, " : ", value)

#output: brand : Ford
#        model : Mustang
#        year : 2018

# Check if key exists

if "model" in thisdict:
    print("Yes, model is one of the keys in thisdict dictionary")

#output: Yes, model is one of the keys in thisdict dictionary

# Dictionary length

print(len(thisdict))

#output: 3

# Adding items to a dictionary

thisdict["color"] = "red"
print(thisdict)

#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}

# Removing items from a dictionary

thisdict.pop("model")
print(thisdict)

#output: {'brand': 'Ford', 'year': 2018, 'color': 'red'}

thisdict.popitem()
print(thisdict)

#output: {'brand': 'Ford', 'year': 2018}

del thisdict["year"]
print(thisdict)

#output: {'brand': 'Ford'}

thisdict.clear()
print(thisdict)

#output: {}