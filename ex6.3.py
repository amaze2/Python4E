def count(x, y):
	num = 0
	for i in word:
		if i == letter:
			num = num + 1
	print(num)
	
word = input("Please enter a word: ")
letter = input("Please enter a letter in word: ")
count(word, letter)
