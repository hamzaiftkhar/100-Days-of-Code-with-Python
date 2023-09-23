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