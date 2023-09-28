"""
### Question-1

Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T"?

```
Test Case:
If the file "story.txt" contains the following lines: 

A boy is playing there.
There is a playground.
An airplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password.

Output:
3
```
"""

# Code:

#Create a file story.txt and write the following lines in it

text = ["A boy is playing there.","There is a playground.","An airplane is in the sky.","The sky is pink.","Alphabets and numbers are allowed in the password."]

file = open("story.txt","w")
for line in text:
    file.write(line+"\n")
file.close()

# Output the content of files
file = open("story.txt","r")
print(file.read())
file.close()

# Function to count the number of lines starting from T.
def line_count():
    file = open("story.txt","r")
    count=0
    for line in file:
        if line[0] in 'T':
            count+= 1
    file.close()
    print("No of lines not starting with 'T'=",count)

line_count()