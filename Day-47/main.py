# examples of getters and setters in python

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

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1
        
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

# input
# 4
# -1
# 10
# 16
# 18

# output
# Age is not valid, setting age to 0.
# You are young.
# You are young.

# You are young.
# You are a teenager.

# You are a teenager.
# You are old.

# You are old.
# You are old.

#---------------------------------------------
# Python program showing a 
# use of property() function 

class Practice: 
	def __init__(self): 
		self._age = 0
	
	# function to get value of _age 
	def get_age(self): 
		print("getter method called") 
		return self._age 
	
	# function to set value of _age 
	def set_age(self, a): 
		print("setter method called") 
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Practice() 

mark.age = 10

print(mark.age) 

#output
# setter method called
# getter method called
# 10

#---------------------------------------------

# Python program showing the use of 
# @property 

class Practice: 
	def __init__(self): 
		self._age = 0
	
	# using property decorator 
	# a getter function 
	@property
	def age(self): 
		print("getter method called") 
		return self._age 
	
	# a setter function 
	@age.setter 
	def age(self, a): 
		if(a < 18): 
			raise ValueError("Sorry you age is below eligibility criteria") 
		print("setter method called") 
		self._age = a 

mark = Practice() 

mark.age = 19

print(mark.age) 

#output
# setter method called
# getter method called
# 19
