d = dict()
val = 0
largest = 0

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		email = words[1]
		d[email] = d.get(email, val) + 1 

for k in d:
	if largest is 0 or d[k]> largest:
		largest = d[k]
		sender = k

print(sender, largest)
		