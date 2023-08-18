#Index Error
"""If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist!"""

# examples of string indexing

string = "Hello World"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])


# Define a sample string
sample_string = "Hello, World!"

# Access individual characters using positive indexing
first_char = sample_string[0]   # 'H'
second_char = sample_string[1]  # 'e'
last_char = sample_string[-1]    # '!'

# Access characters using slicing
substring = sample_string[7:12]     # 'World'
substring_from_start = sample_string[:5]  # 'Hello'
substring_to_end = sample_string[7:]      # 'World!'

# Access characters with step size
every_other_char = sample_string[::2]  # 'Hlo ol!'

# Negative step size for reverse order
reverse_string = sample_string[::-1]  # '!dlroW ,olleH'

# Nested indexing
nested_example = sample_string[3:9][::-1]  # 'loW ,o'

# Find the index of a substring
index_of_comma = sample_string.index(',')  # 5

# Checking if a character is present in the string
is_w_present = 'W' in sample_string  # True
is_z_present = 'z' in sample_string  # False

# Length of the string
string_length = len(sample_string)  # 13

# Define a sample string
sample_string = "Python Programming is Fun"

# Slicing to get words
first_word = sample_string[:6]  # 'Python'
second_word = sample_string[8:19]  # 'Programming'
last_word = sample_string[-3:]  # 'Fun'

# Slicing with steps
every_second_char = sample_string[::2]  # 'Pto rgamn sFn'
reverse_every_third_char = sample_string[::3][::-1]  # 'uPnrimisooPt'

# Slicing with start, end, and step
selected_chars = sample_string[7:18:3]  # 'Pai'

# Reversing a string
reverse_string = sample_string[::-1]  # 'nuF si gnimmargorP nohtyP'

# Slicing to remove words
without_first_word = sample_string[7:]  # 'Programming is Fun'
without_last_word = sample_string[:-4]  # 'Python Programming is'

# Slicing to modify a portion of the string
modified_string = sample_string[:6] + " is Awesome"  # 'Python is Awesome'

# Slicing with step for custom formatting
formatted_string = sample_string[::2] + " " + sample_string[1::2]  # 'Pto rgamn s Fni soii u'

# Splitting and rejoining using slicing
words = sample_string.split()  # ['Python', 'Programming', 'is', 'Fun']
rejoined_string = " ".join(words)  # 'Python Programming is Fun'

# Nested slicing
nested_slice = sample_string[3:18][::2]  # 'hnPormn'

# Slicing with negative indices
negative_slice = sample_string[-7:-2]  # ' is F'

# Slicing with out-of-range indices
out_of_range_slice = sample_string[20:30]  # 'un'