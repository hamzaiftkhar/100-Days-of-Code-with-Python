# Week-6 Review and Our Sixth Challenge Exercise

#### [Day-37](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-37) - File Handling in Python

- Python File Handling
- open() function
- Reading Files
- Deleting Files

#### [Day-38](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-38) - Python Local and Global Variables

- Local Variables
- Global Variables
- Global Keyword
- Difference between Local and Global Variables

#### [Day-39](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-39) - How Import Works in Python

- How Import Works in Python
- Importing a Module Using "as" Keyword
- Importing Specific Functions from a Module
- Importing All Functions from a Module
- The dir() Function
- Importing our self-made modules

#### [Day-40](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-40) - How ```if __name__ == "__main__"``` works in Python?

- How ```if __name__ == "__main__"``` works in Python?
- ```__name__``` variable
- ```__main__``` variable
- Why it is necessary to use ?

#### [Day-41](https://github.com/hamzaiftkhar/100-Days-of-Code-with-Python/tree/main/Day-41) - read, readlines and other file methods

- read() method
- readlines() method
- Read file using loop
- with statement

## Our Sixth Challenge Exercise

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

### Question-2

Write a function in Python to count and display the total number of words in a text file ?

```
Test Case:
If the file contain following items :

Hello world
This is Python Programming
Language

Output:
7
```

### Question-3

A text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#". Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.

```
Test Case:
If the file "matter.txt" contains the following lines:

Hello World

Output:
H#e#l#l#o# #W#o#r#l#d
```

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