# Python String Formatting [format() method]

Python string formatting refers to the process of creating strings that contain placeholders for dynamic values and then replacing those placeholders with actual values. It allows you to create strings that are more flexible and can incorporate variable data, such as numbers, text, or other values, into a larger string.

String formatting in Python allows you to create dynamic strings by combining variables and values.

There are five different ways to perform string formatting in Python:

- Formatting with % Operator.
- Formatting with format() string method.
- Formatting with string literals, called f-strings.
- Formatting with String Template Class
- Formatting with center() string method.

So we will see the entirety of the above-mentioned ways, and we will also focus on which string formatting strategy is the best.

1. ## Formatting with % Operator

The % operator can also be used for string formatting. It interprets the left argument much like a sprintf()-style format string to be applied to the right argument, and returns the string resulting from this formatting operation.

It is the oldest method of string formatting. Here we use the modulo % operator. The modulo % is also known as the “string-formatting operator”.

```python
name = "Hamza"
age = 20
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)
```

Output:

```python
My name is Hamza and I am 20 years old.
```

The % operator can be used with various types of data, such as integers, floats, and strings. It can also be used with tuples, lists, and dictionaries.

```python
x = 'looked'

print("Usman %s and %s around"%('walked',x))
```

Output:

```python
Usman walked and looked around
```

2. ## Formatting using format() Method

The format() method was added in Python(3). It is an alternative to % operator. It allows multiple substitutions and value formatting. It lets us concatenate elements within a string through positional formatting.

```python
name = "Hamza"
age = 20
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
```

Output:

```python
My name is Hamza and I am 20 years old.
```

- #### Index-based Insertion

In this code, curly braces {} with indices are used within the string ‘{2} {1} {0}’ to indicate the positions where the corresponding values will be placed.

```python
print("Usman {2} and {1} around {0}".format('walked','looked','jumped'))
```

Output:

```python
Usman jumped and looked around walked
```

- #### Keyword-based Insertion

In this code, curly braces {} with named placeholders ({a}, {b}, {c}) are used within the string ‘a: {a}, b: {b}, c: {c}’ to indicate the positions where the corresponding named arguments will be placed.

```python
print('a: {a}, b: {b}, c: {c}'.format(a = 1,
									b = 'Two',
									c = 12.3))
```

Output:

```python
a: 1, b: Two, c: 12.3
```

- #### Reuse the inserted objects

In this code, curly braces {} with named placeholders ({p}) are used within the string ‘The first {p} was alright, but the {p} {p} was tough.’ to indicate the positions where the corresponding named argument p will be placed.

```python
print('The first {p} was alright, but the {p} was tough.'.format(p = 'exam'))
```

Output:

```python
The first exam was alright, but the exam was tough.
```

- #### Float Precision with the.format() Method
```
Syntax: {[index]:[width][.precision][type]}

The type can be used with format codes:

- ‘d’ for integers
- ‘f’ for floating-point numbers
- ‘b’ for binary numbers
- ‘o’ for octal numbers
- ‘x’ for octal hexadecimal numbers
- ‘s’ for string
- ‘e’ for floating-point in an exponent format
```

```python
print('The valueof pi is: %1.5f' %3.141592)
print('The valueof pi is: {0:1.5f}'.format(3.141592))
```

Output:

```python
The valueof pi is: 3.14159
The valueof pi is: 3.14159
```

3. ## Understanding Python f-string

Python f-string is the newest Python syntax to do string formatting. It is available in Python 3.6 and above. It is faster than both %-formatting and str.format().

```python
name = "Hamza"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
```

Output:

```python
My name is Hamza and I am 20 years old.
```

- #### Arithmetic operations using F-strings

In this code, the f-string f” He said his age is {2 * (a + b)}.” is used to interpolate the result of the expression 2 * (a + b) into the string.

```python
a = 4
b = 5
print(f"He said his age is {2 * (a + b)}.")
```

Output:

```python
He said his age is 18.
```

- #### Float precision in the f-String Method

In this code, f-string formatting is used to interpolate the value of the num variable into the string.
```
Syntax: {[value]:[width][.precision][type]}
```

```python
num = 3.141592
print(f"The value of pi is {num:{1}.{5}}")
```

Output:

```python
The value of pi is 3.1416
```

4. ## Python String Template Class

In the String module, Template Class allows us to create simplified syntax for output specification. The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing $$ creates a single escaped $:

```python
from string import Template
name = "Hamza"
age = 20
t = Template('My name is $name and I am $age years old.')
print(t.substitute(name=name, age=age))
```

Output:

```python
My name is Hamza and I am 20 years old.
```

5. ## Python String center() Method

The center() method is a built-in method in Python‘s str class that returns a new string that is centered within a string of a specified width. 

```python
string = "100-days-of-code"
width = 30

centered_string = string.center(width)

print(centered_string)
```

Output:

```python
       100-days-of-code
```