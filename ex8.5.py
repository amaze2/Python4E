count = 0
fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		print(words[1])
		count = count + 1
print(count)