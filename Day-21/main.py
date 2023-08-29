def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")


#--------------------------------------------------

def factorial_with_while(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Test the function
num = 5
result = factorial_with_while(num)
print(f"The factorial of {num} is {result}")

#--------------------------------------------------

def factorial_with_for(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the function
num = 5
result = factorial_with_for(num)
print(f"The factorial of {num} is {result}")

#--------------------------------------------------

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test the function
num = 5
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")

#--------------------------------------------------