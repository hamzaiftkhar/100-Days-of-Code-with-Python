# This is our main file:

# Path: Day-39/main.py

import Practice as p
from math import *

print(p.add(2, 3))     # 5
print(p.sub(2, 3))     # -1
print(p.mul(2, 3))     # 6
print(p.div(2, 3))     # 0.6666666666666666
print(p.mod(2, 3))     # 2
print(p.power(2, 3))   # 8
print(p.floor(2, 3))   # 0
p.main()               # This is a practice file.

print(sqrt(4))         # 2.0
print(floor(4.5))      # 4
print(ceil(4.5))       # 5
print(round(4.5))      # 4
print(round(4.6))      # 5

# We can also import specific functions from a module:

# Path: Day-39/main.py

from random import randint, choice

print(randint(1, 10))  

lst = [1, 2, 3, 4, 5]
print(choice(lst))    