# This is a script program tht will be include in the main program

def hello():
    print("I am the Hello function")

def bye():
    print("I am the Bye function")

print(__name__)

if __name__ == "__main__":
    print("This is the Practice program")
    hello()
    bye()



# Now if we separately run this program then it will print the __name__ as __main__ and will print the "This is the Practice program" and will call the hello() and bye() function

# This is the Practice program
# I am the Hello function
# I am the Bye function