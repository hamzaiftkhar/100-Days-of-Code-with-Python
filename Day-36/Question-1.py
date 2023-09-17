"""
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

"""

# Solution 1

def word_frequency_counter(text):
    # Split the text into words
    words = text.split()

    # Create an empty dictionary to store word frequencies
    word_freq = {}

    # Count word frequencies
    for word in words:
        # Remove punctuation and convert to lowercase for case insensitivity
        word = word.strip('.,?!').lower()
        
        if word:
            # Update the word frequency in the dictionary
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

# Example usage:
text = "This is a sample text. This text is just a sample."
result = word_frequency_counter(text)
print(result)

# Output:
# {'this': 2, 'is': 2, 'a': 2, 'sample': 2, 'text': 2, 'just': 1}

"""
EXPLANATION:-

Here's a step-by-step explanation:

1. The input text is: "This is a sample text. This text is just a sample."

2. We split the text into words using .split(), resulting in the following list of words:

['This', 'is', 'a', 'sample', 'text.', 'This', 'text', 'is', 'just', 'a', 'sample.']

3. We initialize an empty dictionary called word_freq to store word frequencies.

4. We iterate through each word in the list of words.

5. For each word, we perform the following operations:

6. We remove punctuation characters (.,?!) using .strip('.,?!'), which results in removing the period and other punctuation marks from the word "text." to make it "text".

7. We convert the word to lowercase using .lower(), making it case-insensitive.

8. After processing, we check if the word is not empty. If it's not empty (to avoid empty strings after stripping punctuation), we update the word frequency in the word_freq dictionary.

9. We use word_freq.get(word, 0) to retrieve the current frequency of the word. If the word is not yet in the dictionary, it defaults to 0.

10. We add 1 to the current frequency, and the updated frequency is assigned back to the word in the word_freq dictionary.

11. The loop continues for all words in the input text, updating their frequencies in the dictionary.

Finally, we return the word_freq dictionary, which contains the word frequencies.

"""