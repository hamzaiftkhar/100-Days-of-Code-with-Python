# Variables and Data Types in Python 

## Variables in Python

**Variable** - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type.

```python
    # variable declaration
    variable_name = value
```
Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.

Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

```python
    a = 10
    b = True
    c = "Harry"
    d = None
 ```
These are four variables of different data types.

## Data Types in Python

**Data Type** - a classification of data which tells the compiler or interpreter how the programmer intends to use the data.

Python has the following data types built-in by default, in these categories:

* Text Type:	str
* Numeric Types:	int, float, complex
* Sequence Types:	list, tuple, range
* Mapping Type:	dict
* Set Types:	set, frozenset
* Boolean Type:	bool
* Binary Types:	bytes, bytearray, memoryview

By default, python provides the following built-in data types:

#### 1. Numeric data: int, float, complex
     int: 3, -8, 0
     float: 7.349, -9.0, 0.0000001
     complex: 6 + 2i

#### 2. Text data: str

    str: "Hello World!!!", "Python Programming"

#### 3. Boolean data:
    Boolean data consists of values True or False.

#### 4. Sequenced data: list, tuple 

**list:** A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

**Example:**
```python 
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```
Output:

```python
    [8, 2.3, [-4, 5], ['apple', 'banana']]
```

**Tuple:** A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

**Example:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

Output:
    
```python
    (('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

#### 5. Mapped data: dict
**dict:** A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

**Example:**
```python
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
```
Output:
```python
    {'name': 'Sakshi', 'age': 20, 'canVote': True}
```

## Type Conversion in Python

**Type Conversion** - The conversion of one data type into another data type.

#### Implicit Conversion
 When the Python interpreter automatically converts one data type to another.

#### Explicit Conversion 
When code is written to manually convert one data type to another using a data type conversion function:

- **str()** - converts a value (often numeric) to a **string** data type.

- **int()** - converts a value (usually a float) to an **integer** data type.

- **float()** - converts a value (usually an integer) to a **float** data. type

- **bool()** - converts a value to a **boolean** data type.

Examples of Explicit Conversion:

```python
 # int to float
a = 10
b = float(a)
print(b)
```
Output:
```python
    10.0
``````
## Type() Function

**type()** - a built-in function used to determine the data type of a variable or value.

```python
    # type() function
    type(variable_name)
```
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

```python
a = 1
print(type(a))
b = "1"
print(type(b))
```
Output:
```python
    <class 'int'>
    <class 'str'>
```