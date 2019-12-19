list = []
fhand = open("romeo.txt")
for line in fhand:
	words = line.split()
	for word in words:
		if word not in list:
			list.append(word)
list.sort()
print(list)
			
	