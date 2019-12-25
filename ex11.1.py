def grep():
	count = 0
	import re
	file = input("Please enter a file to be searched: ")
	fhand = open(file)
	regex = input("Please enter a regular expression: ")
	for line in fhand:
		x = re.findall(regex, line)
		if len(x) >0:
			count = count + 1
			print(x)
	print(count)

			
			

grep()
	