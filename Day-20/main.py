# Examples of Recursion

# Python3 program to Print
# numbers from 1 to n


def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')


# Driver code
n = 10
printNos(n)

#--------------------------------------------------------------

#factorial calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
#--------------------------------------------------------------

#fibonacci series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print(result)  # Output: 8 (fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...)
#--------------------------------------------------------------

#sum of digits
def sum_list_elements(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list_elements(lst[1:])

my_list = [1, 2, 3, 4, 5]
result = sum_list_elements(my_list)
print(result)  # Output: 15
#--------------------------------------------------------------

#power of a number
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

result = power(2, 3)
print(result)  # Output: 8 (2^3)
#--------------------------------------------------------------

#binary search
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
result = binary_search(my_list, target, 0, len(my_list) - 1)
print(result)  # Output: 6 (index of target in the list)
#--------------------------------------------------------------

def head_recursion_example(n):
    if n > 0:
        head_recursion_example(n - 1)  # Recursive call before processing
        print(n)

head_recursion_example(3)
# Output:
# 1
# 2
# 3

#--------------------------------------------------------------

def tail_recursion_example(n):
    if n > 0:
        print(n)
        tail_recursion_example(n - 1)  # Recursive call is the last operation

tail_recursion_example(3)
# Output:
# 3
# 2
# 1

#--------------------------------------------------------------

def nested_recursion(n):
    if n > 100:
        return n - 10
    else:
        return nested_recursion(nested_recursion(n + 11))

result = nested_recursion(95)
print(result)  # Output: 91

#--------------------------------------------------------------
def tree_recursion(n):
    if n > 0:
        print(n)
        tree_recursion(n - 1)
        tree_recursion(n - 1)

tree_recursion(3)
# Output:
# 3
# 2
# 1
# 1
# 2
# 1
# 1

#--------------------------------------------------------------