"""
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
"""

# Solution:

def merge_dictionaries(dict1, dict2):
    merged_dict = {}

    # Merge values from the first dictionary
    for key, value in dict1.items():
        merged_dict[key] = value

    # Merge values from the second dictionary, combining if keys already exist
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key already exists in the merged dictionary, create a list
            # if it's not already a list and add the new value to the list.
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value

    return merged_dict

# Example usage:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5, "e": 6}

result = merge_dictionaries(dict1, dict2)
print(result)

# Output:
# {'a': 1, 'b': [2, 4], 'c': 3, 'd': 5, 'e': 6}

"""
EXPLANATION:-

Here's a step-by-step explanation:

1. The input dictionaries are:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5, "e": 6}

2. We initialize an empty dictionary called merged_dict to store the merged dictionary.

3. We iterate through each key-value pair in the first dictionary and add it to the merged dictionary.

4. We iterate through each key-value pair in the second dictionary and add it to the merged dictionary. If the key already exists in the merged dictionary, we combine the values into a list.

5. The merged dictionary is returned.

"""
