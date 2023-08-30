"""
Write a program to print the following star pattern using the for loop?

* * * * *
* * * *
* * *
* *
*
"""

# Code:

def pattern(n):
    for i in range(n, 0, -1):   # 5, 4, 3, 2, 1
        for j in range(0, i):   # loop will run 5, 4, 3, 2, 1 times
            print("* ", end="")    # print * and space
        print("\r")    # print new line

pattern(5)