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

## Object of a class

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. It’s not an idea anymore, it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many dogs to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of:

- **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
- **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
- **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

## Example of Python class and object

```python

# Python3 program to
# demonstrate instantiating
# a class
class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()
```

**OUTPUT**

```python
mammal
I'm a mammal
I'm a dog
```

In the above example, an object is created which is basically a dog named Rodger. This class only has two class attributes that tell us that Rodger is a dog and a mammal. The method fun() tells us that the dog can state its identity. This is how an object is created and used.

## __init__() method

The ```__init__``` method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

**Example:**

```python
# Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Python')
p.say_hi()
```

**OUTPUT**

```python
Hello, my name is Python
```

In the above example, we define a class named Person. The ```__init__``` method is used to initialize the object’s state. The ```self``` parameter refers to the instance of the object itself. The ```self``` parameter is used to access variables that belong to the class. It is used to access methods also.

## Self Parameter

class CS:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show(self):
        print("Hello my name is " + self.name+" and I" +
            " am studying "+self.subject+".")


obj = CS("hamza", "Python Programming")
obj.show()
```

**OUTPUT**

```python
Hello my name is hamza and I am studying Python Programming.
```

In the above example, we define a class named CS. The ```__init__``` method is used to initialize the object’s state. The ```self``` parameter refers to the instance of the object itself. The ```self``` parameter is used to access variables that belong to the class. It is used to access methods also.

