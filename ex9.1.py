wordcount = dict()
fhand = open("words.txt")
fread = fhand.read()
words = fread.split()
for word in words:
	wordcount[word] = wordcount.get(word, 0)
print(wordcount)
close("words.txt")