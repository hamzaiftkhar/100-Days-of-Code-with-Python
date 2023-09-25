# Python program to
# demonstrate with
# statement

L = ["Python\n", "for\n", "Fun\n"]


# Writing to file
with open("myfile.txt", "w") as fp:
	fp.writelines(L)


# using readlines()
count = 0
print("Using readlines()")

with open("myfile.txt") as fp:
	Lines = fp.readlines()
	for line in Lines:
		count += 1
		print("Line{}: {}".format(count, line.strip()))


# Using readline()
count = 0
print("\nUsing readline()")

with open("myfile.txt") as fp:
	while True:
		count += 1
		line = fp.readline()

		if not line:
			break
		print("Line{}: {}".format(count, line.strip()))


# Using for loop
count = 0
print("\nUsing for loop")

with open("myfile.txt") as fp:
	for line in fp:
		count += 1
		print("Line{}: {}".format(count, line.strip()))

