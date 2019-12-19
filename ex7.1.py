filename = input("Please enter the filename: ")
fhand = open(filename)
for line in fhand:
	line = line.rstrip().upper()
	print(line)