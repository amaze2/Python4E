count = 0
val = 0
d = dict()
lst = list()

fhand = open("mbox-short.txt")
for line in fhand:
	if line.startswith("From "):
		words = line.split()
		email = words[1]
		d[email] = d.get(email, val) + 1 

for k,v in d.items():
	lst.append( (v,k) )
lst.sort(reverse = True)
print(max(lst))