# " if __name__ == "__main__" works in Python

The if ```__name__ == "__main__"``` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the ```__name__``` variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the ```__name__``` variable is set to the string ```__main__``` When the script is imported as a module into another script, the ```__name__ ``` variable is set to the name of the module.

Here's an example of how the if ```__name__ == __main__``` idiom can be used:

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

In the above example, the my_module.py script is run directly, so the ```__name__``` variable is set to ```__main__``` and the if ```__name__ == __main__``` condition is satisfied, so the code inside the if statement is executed.

When the my_module.py script is imported as a module into the main.py script, the ```__name__``` variable is set to the name of the module, which is my_module. Since the ```__name__``` variable is not set to ```__main__```, the code inside the if statement is not executed.

The if ```__name__ == __main__``` idiom is useful when you want to be able to run a Python script both directly and via import without having unwanted side effects.

For example, if you have a script that performs some calculations and prints the results to the console, you may want to be able to import the script into another script without having the calculations and print statements run automatically.

The if ```__name__ == __main__``` idiom allows you to do this by placing the code that you want to run only when the script is run directly inside the if statement.

## Why it is necessary to use ?

The if ```__name__ == __main__``` idiom is not strictly necessary, but it is considered good practice to use it in Python scripts.

The reason for this is that when you import a Python script as a module into another script, the code in the imported script is executed immediately.

This can cause unwanted side effects if the imported script contains code that performs calculations or prints output to the console.

The if ```__name__ == __main__``` idiom allows you to prevent this from happening by placing the code that you want to run only when the script is run directly inside the if statement.

- ### Example

Suppose you make a script file which deletes some files in a folder. Now you want to use this script in another script. So you import this script in another script. But when you import this script, it will delete the files in the folder automatically just after importing. Because on importing it will run the whole script without doing anything in new script. 

So to prevent this, we use if ```__name__ == "__main__"``` in the script file. So when we import this script in another script, it will not run the whole script.

```python
def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
```

```python
import script

print("Importing script")
```

Output:

```python
Importing script
```

In the above example, the script.py script is run directly, so the ```__name__``` variable is set to ```__main__``` and the if ```__name__ == __main__``` condition is satisfied, so the code inside the if statement is executed.

When the script.py script is imported as a module into the main.py script, the ```__name__``` variable is set to the name of the module, which is script. Since the ```__name__``` variable is not set to ```__main__```, the code inside the if statement is not executed.

## Important Concept

Consider the following example:

```python
def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
```

```python
import script

print("Importing script")
```

Output:

```python
Importing script
```

Here ```__name__``` is a built-in variable which evaluates to the name of the current module. However, if a module is being run directly (as in the case of script.py above), then ```__name__``` instead is set to the string ```__main__```.

- If the script is run directly where the script is the entry point, then ```__name__``` is set to ```__main__```.
- If the script is imported as a module into another script, then ```__name__``` is set to the name of the module.

Example:

```python
# script.py

print(__name__)
```

```python
# main.py

import script
```

Now if we run the script.py file, we will get the following output:

```python
__main__
```

And if we run the main.py file, we will get the following output:

```python
script
```

## Conclusion

The if ```__name__ == __main__``` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the ```__name__``` variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the ```__name__``` variable is set to the string ```__main__``` When the script is imported as a module into another script, the ```__name__ ``` variable is set to the name of the module.

The if ```__name__ == __main__``` idiom is useful when you want to be able to run a Python script both directly and via import without having unwanted side effects.

The if ```__name__ == __main__``` idiom is not strictly necessary, but it is considered good practice to use it in Python scripts.

The reason for this is that when you import a Python script as a module into another script, the code in the imported script is executed immediately without doing anything in new script.And this will be a problem if the imported script contains code that performs calculations or prints output to the console.

The if ```__name__ == __main__``` idiom allows you to prevent this from happening by placing the code that you want to run only when the script is run directly inside the if statement.