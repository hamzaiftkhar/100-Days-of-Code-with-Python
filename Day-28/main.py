# Examples of List and Tuples

students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [92, 88, 95]},
    {"name": "Charlie", "age": 21, "grades": [78, 85, 80]},
    {"name": "David", "age": 23, "grades": [88, 92, 87]},
]

# You can access individual student records and their grades like this:
alice_grades = students[0]["grades"]
charlie_age = students[2]["age"]


todo_list = [
    {"task": "Buy groceries", "priority": "High"},
    {"task": "Finish project report", "priority": "Medium"},
    {"task": "Exercise", "priority": "Low"},
    {"task": "Call mom", "priority": "High"},
]

# You can add, remove, or update tasks in the to-do list.
todo_list.append({"task": "Read a book", "priority": "Low"})
todo_list[1]["task"] = "Complete project report"


point = (3, 4)

# You can access individual elements of the tuple:
x = point[0]
y = point[1]

# Tuples are often used to represent coordinates or 2D points.


from collections import namedtuple

# Define a named tuple class
Person = namedtuple("Person", ["name", "age", "occupation"])

# Create instances of the named tuple
alice = Person("Alice", 30, "Engineer")
bob = Person("Bob", 25, "Designer")

# Access fields using named attributes
alice_name = alice.name
bob_age = bob.age