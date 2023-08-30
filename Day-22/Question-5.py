"""
Question-5:
Write a recursive function to print the reverse of a given string.

Test Data:

Input: Hello
Output: olleH

Input: 123456789
Output: 987654321
"""

# Code:

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]
    
print(reverse_string("Hello"))
print(reverse_string("123456789"))
