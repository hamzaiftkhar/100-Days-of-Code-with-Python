# Examples of file handling

# Reading a file
file = open("file.txt", "r")
print(file.read())
file.close()

# Writing a file
file = open("file.txt", "w")
file.write("Hello World!")
file.close()

# Appending a file
file = open("file.txt", "a")
file.write("\nHello World!")
file.close()

# Reading a file line by line
file = open("file.txt", "r")
print(file.readline())
print(file.readline())
file.close()

# Reading a file line by line using for loop
file = open("file.txt", "r")
for line in file:
    print(line)
file.close()
