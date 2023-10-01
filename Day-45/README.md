# Classes and objects in python

## Class

A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

**Syntax: Class definition**

```python
class ClassName:
    #Statements
```

**Syntax: Object definition**

```python
object_name = ClassName()
print(object_name)
```

**Some points on Python class:**

- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute.

### Creating a class

```python
class CS:
    subject = "Computer Science"
```