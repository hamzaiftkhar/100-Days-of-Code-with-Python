# Recursion in Python

## What is Recursion?

Recursion is the process of defining something in terms of itself. In programming languages, if a program allows you to call a function inside the same function, then it is called a recursive call of the function.

## Properties of Recursion:
Recursion has some important properties. Some of which are mentioned below:

- The primary property of recursion is the ability to solve a problem by breaking it down into smaller sub-problems, each of which can be solved in the same way.
- A recursive function must have a base case or stopping criteria to avoid infinite recursion.
- Recursion involves calling the same function within itself, which leads to a call stack.
- Recursive functions may be less efficient than iterative solutions in terms of memory and performance.

Syntax of Recursion:
```python
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```

Example of Recursion:

```python
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
```

Output:
```python
Recursion Example Results
1
3
6
10
15
21
```

## Advantages of Recursion:

- Recursion can simplify complex problems by breaking them down into smaller, more manageable pieces.
- Recursive code can be more readable and easier to understand than iterative code.
- Recursion is essential for some algorithms and data structures.
- Also with recursion, we can reduce the length of code and become more readable and understandable to the user/ programmer.

## Disadvantages of Recursion:

- Recursion can be less efficient than iterative solutions in terms of memory and performance.
- Recursive functions can be more challenging to debug and understand than iterative solutions.
- Recursion can lead to stack overflow errors if the recursion depth is too high.