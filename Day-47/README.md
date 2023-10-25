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