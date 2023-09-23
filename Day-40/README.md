# " if __name__ == "__main__" works in Python

The if **__name__ == "__main__"** idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

Here's an example of how the if __name__ == __main__ idiom can be used:

```python
# my_module.py

def say_hello():
    print("Hello, I'm a function")

print("Hello, I'm the main script")

if __name__ == "__main__":
    print("Hello, I'm the main script")
    say_hello()
```

```python
# main.py

import my_module

print("Hello, I'm the main script")

my_module.say_hello()
```

Output:

```python
# Output

Hello, I'm the main script
Hello, I'm the main script
Hello, I'm a function
```

In the above example, the my_module.py script is run directly, so the __name__ variable is set to __main__ and the if __name__ == __main__ condition is satisfied, so the code inside the if statement is executed.

When the my_module.py script is imported as a module into the main.py script, the __name__ variable is set to the name of the module, which is my_module. Since the __name__ variable is not set to __main__, the code inside the if statement is not executed.

The if __name__ == __main__ idiom is useful when you want to be able to run a Python script both directly and via import without having unwanted side effects.

For example, if you have a script that performs some calculations and prints the results to the console, you may want to be able to import the script into another script without having the calculations and print statements run automatically.

The if __name__ == __main__ idiom allows you to do this by placing the code that you want to run only when the script is run directly inside the if statement.