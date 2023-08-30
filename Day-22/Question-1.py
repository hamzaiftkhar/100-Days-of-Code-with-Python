"""
Question-1:
Write a program to print the following star pattern using the for loop?

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

# Code:

def pattern(n):
    for i in range(0, n):   # 0, 1, 2, 3, 4
        for j in range(0, i+1):   # loop will run 1, 2, 3, 4, 5 times
            print("* ", end="")    # print * and space
        print("\r")    # print new line
    for i in range(n, 0, -1):     # 5, 4, 3, 2, 1
        for j in range(0, i-1):   # loop will run 4, 3, 2, 1, 0 times
            print("* ", end="")   # print * and space
        print("\r")    # print new line

pattern(5)