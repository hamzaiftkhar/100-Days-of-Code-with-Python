# Examples 

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


# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)




# Python3 program to show that we can create
# instance variables inside methods

# Class for Dog


class Dog:

	# Class Variable
	animal = 'dog'

	# The init method or constructor
	def __init__(self, breed):

		# Instance Variable
		self.breed = breed

	# Adds an instance variable
	def setColor(self, color):
		self.color = color

	# Retrieves instance variable
	def getColor(self):
		return self.color


# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

p1.age = 40

print(p1.age)

del p1.age