# Getters and Setters in Python

## What are Getters and Setters?

Getters and Setters are used to protect your data, particularly when creating classes. Getters are used to get the value of a variable, while setters are used to set the value of a variable.

## Why use getters and setters?

It is good practice to use getters and setters in your classes, even if you don't need to implement any functionality in them yet. Why? Because it allows you to easily add functionality to the getters and setters without changing the public interface of your class. This is important because there may be code outside of your class that depends on the interface of your class.

## Example

Let's say you have a class called `Person`. This class has a variable called `age`. You want to make sure that the age is never negative. You can do this by using a setter.

```python
class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def getAge(self):
        return self.age

    def setAge(self, newAge):
        if newAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = newAge
```

Now, if you want to change the implementation of the `setAge` method, you can do so without changing the interface of the `Person` class. For example, you could change it to this:

```python
def setAge(self, newAge):
    self.age = newAge
```

This would allow you to set the age to a negative number, which is not what you want. But you can change the implementation of the `setAge` method without changing the interface of the `Person` class.

## Using Getters and Setters

To achieve getters & setters property, if we define normal get() and set() methods it will not reflect any special implementation. 

**For Example:**

```python
class Person:
    def __init__(self, initialAge):
        self.age = initialAge

    def getAge(self):
        return self.age

    def setAge(self, newAge):
        self.age = newAge
```

Now, if we want to set the age of a person, we can use the setter method. 

```python
person = Person(10)
person.setAge(20)
print(person.getAge())
```

This will print `20`.

But, if we want to set the age of a person, we can use direct set method. 

```python
person = Person(10)
person.age = 20
print(person.age)
```

This will also print `20`. So, there is no difference between using the setter method and directly setting the value of the variable.

## Using property() function

To achieve getters & setters property, we can use the `property()` function. The `property()` function returns a property object. The property object has three methods, `getter()`, `setter()`, and `deleter()` to specify `fget`, `fset` and `fdel` function.

**Syntax:**

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

**Example:**

```python
class Person:
    def __init__(self, initialAge):
        self.age = initialAge

    def getAge(self):
        return self.age

    def setAge(self, newAge):
        self.age = newAge

    age = property(getAge, setAge)
```

Now, if we want to set the age of a person, we can use the setter method. 

```python
person = Person(10)
person.setAge(20)
print(person.getAge())
```

This will print `20`.

## Using @property decorator

To achieve getters & setters property, we can use the `@property` decorator. The `@property` decorator is used to customize getters and setters for class attributes.

**Example:**

```python
class Person:
    def __init__(self, initialAge):
        self.age = initialAge

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newAge):
        self._age = newAge
```

Now, if we want to set the age of a person, we can use the setter method. 

```python
person = Person(10)
person.age = 20
print(person.age)
```

This will print `20`.

The main function of using property function and @property decorator is to make the code more readable and maintainable. It is not necessary to use them. You can use the normal get() and set() methods to achieve the same functionality. But, it is a good practice to use them.