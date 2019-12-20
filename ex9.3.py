d = dict()

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		email = words[1]
		d[email] = d.get(email, 0) + 1
print(d)
		