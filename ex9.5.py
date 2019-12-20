d = dict()
val = 0

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		email = words[1]
		email = email.split("@")
		domain = email[1]
		d[domain] = d.get(domain, val) + 1 


print(d)
		