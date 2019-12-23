import string
d = dict()
lst = list()

fname = input("Please enter a text filename to be analyzed: ")
fhand = open(fname)

for line in fhand:
	line = line.translate(str.maketrans("", "", string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		t = tuple(word)
		for letter in t:
			d[letter] = d.get(letter, 0) + 1

for k,v in d.items():
	lst.append( (v,k) )
lst.sort(reverse = True)
for k, v in lst:
	print(v, k)

