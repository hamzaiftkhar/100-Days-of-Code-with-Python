"""
### Question-5

A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].

i. Write a user defined function createFile() to input data for a record and add to Book.dat.

ii. Write a function countRec(Author) in Python which accepts the Author name as parameter and count and return number of books by the given Author are stored in the binary file "Book.dat"

iii. Write a function maxRec() in Python to find and display the details of the book with highest price from the binary file "Book.dat".

```
Test Case:

If the file "Book.dat" contains the following lines:

101, Python Programming, Reema Thareja, 450.0
102, C Programming, Ajay Mittal, 250.0
103, Data Structures, Sartaj Sahni, 350.0
104, Java Programming, Reema Thareja, 150.0

Output:
Enter Book Number: 105
Enter Book Name: C++ Programming
Enter Author Name: Reema Thareja
Enter Price: 550.0

Enter Author Name to search: Reema Thareja
Number of books by Reema Thareja are 3

Book with maximum price:
105, C++ Programming, Reema Thareja, 550.0
```
"""

# Code:

#Create a file Book.dat and write the following lines in it

# text = ["101, Python Programming, Reema Thareja, 450.0","102, C Programming, Ajay Mittal, 250.0","103, Data Structures, Sartaj Sahni, 350.0","104, Java Programming, Reema Thareja, 150.0"]

# file = open("Book.dat","w")
# for line in text:
#     file.write(line+"\n")
# file.close()

# def createFile():
#     file = open("Book.dat","ab")
#     BookNo = int(input("Enter Book Number: "))
#     Book_Name = input("Enter Book Name: ")
#     Author = input("Enter Author Name: ")
#     Price = float(input("Enter Price: "))
#     record = [BookNo,Book_Name,Author,Price]
#     pickle.dump(record,file)
#     file.close()

# def countRec(Author):
#     file = open("Book.dat","rb")
#     count = 0
#     try:
#         while True:
#             record = pickle.load(file)
#             if record[2] == Author:
#                 count+=1
#     except EOFError:
#         pass
#     print("Number of books by",Author,"are",count)
#     file.close()

# def maxRec():
#     file = open("Book.dat","rb")
#     max = 0
#     try:
#         while True:
#             record = pickle.load(file)
#             if record[3] > max:
#                 max = record[3]
#                 max_record = record
#     except EOFError:
#         pass
#     print("Book with maximum price:")
#     print(max_record)
#     file.close()

# createFile()

# countRec("Reema Thareja")

# maxRec()
