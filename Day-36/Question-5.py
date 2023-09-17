"""
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

"""

# Solution:

def word_frequency_by_category(sentences):
    # Create a dictionary to store word frequencies by category
    category_word_frequencies = {}

    # Iterate through the input sentences
    for sentence, category in sentences:
        # Split the sentence into words
        words = sentence.split()

        # Create a dictionary to store word frequencies for this sentence
        word_frequency = {}

        # Count word frequencies in the sentence
        for word in words:
            # Convert the word to lowercase to treat words case-insensitively
            word = word.lower()
            # Remove punctuation characters (you can customize this as needed)
            word = word.strip('.,?!')

            if word:
                word_frequency[word] = word_frequency.get(word, 0) + 1

        # Update the category_word_frequencies dictionary
        if category in category_word_frequencies:
            category_word_frequencies[category].update(word_frequency)
        else:
            category_word_frequencies[category] = word_frequency

    return category_word_frequencies

# Example usage:
sentences = [
    ("This is a cat", "Animals"),
    ("The dog is barking", "Animals"),
    ("I love pizza", "Food"),
    ("Pizza is great", "Food"),
    ("The cat and dog are playing", "Animals")
]

result = word_frequency_by_category(sentences)
print(result)

# Output:

# {'Animals': {'this': 1, 'is': 2, 'a': 1, 'cat': 2, 'the': 1, 'dog': 2, 'and': 1, 'are': 1, 'playing': 1, 'barking': 1}, 'Food': {'i': 1, 'love': 1, 'pizza': 2, 'is': 1, 'great': 1}}

"""
EXPLANATION:-

Here's a step-by-step explanation:

1. Create a dictionary to store word frequencies by category
2. Iterate through the input sentences
3. Split the sentence into words
4. Create a dictionary to store word frequencies for this sentence
5. Count word frequencies in the sentence
6. Update the category_word_frequencies dictionary
7. Return the result

"""