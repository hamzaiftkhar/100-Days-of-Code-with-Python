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

## Types of Recursion:

1. **Direct recursion:** When a function is called within itself directly it is called direct recursion. This can be further categorised into four types: 

- Tail recursion,  
- Head recursion,  
- Tree recursion and 
- Nested recursion.

2. **Indirect recursion:** Indirect recursion occurs when a function calls another function that eventually calls the original function and it forms a cycle.

## 1. Direct Recursion:

- ### Tail Recursion:

 If a recursive function calling itself and that recursive call is the last statement in the function then it’s known as Tail Recursion. After that call the recursive function performs nothing. The function has to process or perform any operation at the time of calling and it does nothing at returning time.

```python
def tailRecursion(n):
    if n == 0:
        return
    else:
        print(n)
        tailRecursion(n-1)
```

- Time Complexity For Tail Recursion : **O(n)**
- Space Complexity For Tail Recursion : **O(n)**

- ### Head Recursion:

 If a recursive function calling itself and that recursive call is the first statement in the function then it’s known as Head Recursion. There’s no statement, no operation before the call. The function doesn’t have to process or perform any operation at the time of calling and all operations are done at returning time.

```python
# Python program showing Head Recursion
# Recursive function
def fun(n):

    if (n > 0):

        # First statement in the function
        fun(n - 1)

        print(n,end=" ")

# Driver code
x = 3
fun(x)
```

- Time Complexity For Tail Recursion : **O(n)**
- Space Complexity For Tail Recursion : **O(n)**

- ### Tree Recursion:

 To understand Tree Recursion let’s first understand Linear Recursion. If a recursive function calling itself for one time then it’s known as Linear Recursion. Otherwise if a recursive function calling itself for more than one time then it’s known as Tree Recursion.

```python
# Python program showing Tree Recursion
# Recursive function
# C++ program to show Tree Recursion
# Recursive function
def fun(n):

    if (n > 0):

        print(n, end=" ")

        # Calling once
        fun(n - 1)

        # Calling twice
        fun(n - 1)

# Driver code
fun(3)
```

Output:
```python
3 2 1 1 2 1 1
```

- Time Complexity For Tree Recursion: **O(2^n)**
- Space Complexity For Tree Recursion: **O(n)**

- ### Nested Recursion:

In this recursion, a recursive function will pass the parameter as a recursive call. That means “recursion inside recursion”. Let see the example to understand this recursion.

```python

# Python program showing Nested Recursion
# Recursive function
# Python program to show Nested Recursion
def fun(n):

    if (n > 100):
        return n - 10

    # A recursive function passing parameter
    # as a recursive call or recursion inside
    # the recursion
    return fun(fun(n + 11))

# Driver code
r = fun(95)
print("", r)
```

Output:

```python
91
```

- Time Complexity For Nested Recursion: **O (2^ (n/3))**
- Space Complexity For Nested Recursion: **O(n^2)**

## 2. Indirect Recursion:

Indirect recursion occurs when a function calls another function that eventually calls the original function and it forms a cycle.

```python
# Python program to show Indirect Recursion
def funA(n):
    if (n > 0):
        print("", n, end='')

        # Fun(A) is calling fun(B)
        funB(n - 1)

def funB( n):
    if (n > 1):
        print("", n, end='')

        # Fun(B) is calling fun(A)
        funA(n // 2)

# Driver code
funA(20)
```

Output:

```python
20 19 9 8 4 3 1
```

## Applications of Recursion:

Recursion is used in many fields of computer science and mathematics, which includes:

- Searching and sorting algorithms: Recursive algorithms are used to search and sort data structures like trees and graphs.
- Mathematical calculations: Recursive algorithms are used to solve problems such as factorial, Fibonacci sequence, etc.
- Compiler design: Recursion is used in the design of compilers to parse and analyze programming languages.
- Graphics: many computer graphics algorithms, such as fractals and the Mandelbrot set, use recursion to generate complex patterns.
- Artificial intelligence: recursive neural networks are used in natural language processing, computer vision, and other AI applications.