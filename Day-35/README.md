# Week-5 Review and Our Fifth Challenge Exercise

#### [Day-30](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-30) - Introduction to Dictionaries in Python

- What is a Dictionary?
- Creating a Dictionary
- Adding and Accessing elements to a Dictionary
- looping through a Dictionary

#### [Day-31](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-31) - Dictionary methods in Python Programming Language

- Python Dictionary Methods
- Copying a string

#### [Day-32](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-32) - Sets in Python Programming Language

- What are Sets in Python?
- Creating and Adding element in a Set in Python
- Frozen set in Python
- Advantages and Disadvantages of Sets in Python

#### [Day-33](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-33) - Python - Set Methods

- Set Methods in Python
- Time Complexity of Sets
- Operators in Sets
- Difference between Set and list

#### [Day-34](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-34) - Exception Handling in Python

- Different types of exceptions in python
- Try and Except Statement – Catching Exceptions
- Catching Specific Exceptions in Python
- Try with Else clause and Finally clause
- Advantages and Disadvantages of Exception Handling


# Week-5 Review and Our Fifth Challenge Exercise

## Question 1

Write a Python function that takes a string as input and returns a dictionary where the keys are unique words in the string, and the values are the frequency of each word in the string. Ignore punctuation and consider words in a case-insensitive manner.

For example, if the input string is:

```python
text = "This is a sample text. This text is just a sample."
```

The function should return:

```python
{
    "this": 2,
    "is": 2,
    "a": 2,
    "sample": 2,
    "text": 2,
    "just": 1
}
```

## Question 2

Write a Python function that takes two dictionaries as input and returns a new dictionary that is a merger of the two dictionaries. If there are any overlapping keys, combine their values into a list in the merged dictionary.

For example:

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5, "e": 6}
```

The function should return:

```python
{
    "a": 1,
    "b": [2, 4],
    "c": 3,
    "d": 5,
    "e": 6
}
```

## Question 3

Write a Python function that takes two strings as input and returns a set containing all the characters that are common to both strings, ignoring spaces and case sensitivity.

For example:

```python
str1 = "Hello World"
str2 = "wonderful"
```

The function should return the set:

```python
{'o', 'l', 'r', 'd', 'w'}
```

## Question 4

Given three sets A, B, and C, write a Python function that determines whether C is a subset of both A and B simultaneously.

For example:

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {3, 4}
```

The function should return True because C is a subset of both A and B.

## Question 5

**Problem: Word Frequency by Category**

You are given a list of sentences, where each sentence is associated with a category. Your task is to create a Python function that calculates the word frequency for each category and returns a dictionary where the keys are categories and the values are dictionaries containing word frequencies within each category.

Here's the function signature:

```python
def word_frequency_by_category(sentences):
    # Your code here
    pass
```

The input sentences is a list of tuples, where each tuple contains a sentence (a string) and its associated category (a string).

For example:

```python
sentences = [
    ("This is a cat", "Animals"),
    ("The dog is barking", "Animals"),
    ("I love pizza", "Food"),
    ("Pizza is great", "Food"),
    ("The cat and dog are playing", "Animals")
]
```

Your function should return a dictionary like this:

```python
{
    "Animals": {"This": 1, "is": 2, "a": 1, "cat": 2, "The": 1, "dog": 2, "and": 1, "are": 1, "playing": 1, "barking": 1},
    "Food": {"I": 1, "love": 1, "pizza": 2, "is": 1, "great": 1}
}
```

In this example, the function calculates the word frequency for each category, and the keys in the outer dictionary are the category names ("Animals" and "Food"). The inner dictionaries contain word frequencies for each category.
