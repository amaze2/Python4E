d = dict()
counts = 0

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		day = words[2]
		d[day] = d.get(day, counts) + 1
print(d)
		