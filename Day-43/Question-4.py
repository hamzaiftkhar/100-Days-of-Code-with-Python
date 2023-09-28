"""
### Question-4

A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage). Write a function count_rec() in Python that would read contents of the file "STUDENT.DAT" and display the details of those students whose percentage is above 75. Also display number of students scoring above 75%?

```
Test Case:

If the file "STUDENT.DAT" contains the following lines:

101, Ali, 76.50
102, Roman, 43.0
103, Seema, 85.75
104, Smith, 71.0
105, John, 55.50

Output:
101, Ali, 76.50
103, Seema, 85.75
Number of students scoring above 75% is 2
```
"""

# Code:

#Create a file STUDENT.DAT and write the following lines in it

# text = ["101, Ali, 76.50","102, Roman, 43.0","103, Seema, 85.75","104, Smith, 71.0","105, John, 55.50"]

# file = open("STUDENT.DAT","w")
# for line in text:
#     file.write(line+"\n")
# file.close()

# def count_rec():
#     file = open("STUDENT.DAT","rb")
#     count = 0
#     try:
#         while True:
#             record = pickle.load(file)
#             if record[2] > 75:
#                 print(record)
#                 count+=1
#     except EOFError:
#         pass
#     print('No of students having more than 75% are', count)
#     file.close()