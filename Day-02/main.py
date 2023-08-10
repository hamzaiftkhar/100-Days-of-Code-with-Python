# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)
# The value of pi is 3.141592653589793

# use math.sqrt to get square root of a number
print("The square root of 16 is", math.sqrt(16))
# The square root of 16 is 4.0


#------------------------------------------------------------

# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793

#------------------------------------------------------------

# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793

#------------------------------------------------------------

# we can install multiple pip packages for different projects according to their requirements

# pip install <package-name>   (basic syntax to install a package)

# pip install <package-name>==<version-number>   (to install a specific version of a package)

# pip install <package-name> --upgrade   (to upgrade a package to its latest version)

# pip uninstall <package-name>   (to uninstall a package)

# pip list   (to list all the packages installed in the current environment)

# pip freeze   (to list all the packages installed in the current environment along with their version)

# pip freeze > requirements.txt   (to save all the packages installed in the current environment in a file named requirements.txt)

# Examples of some packages

# pip install numpy
# pip install pandas
# pip install matplotlib    (to plot graphs)
# pip install pandas
# pip install requests
# pip install tensorflow
# pip install os
# pip install cv2
# pip install turtle

# along with these packages, we can also install some IDEs like PyCharm, Spyder, Jupyter Notebook, etc.
# we use these packages to make our work easier and faster
