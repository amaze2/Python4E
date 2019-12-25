tot = 0
count = 0
avg = 0
import re
fhand = open("mbox-short.txt")
for line in fhand:
	x = re.findall("^New Revision: ([0-9]+)", line)
	if len(x) > 0:
		for i in x:
			i = float(i)
		count = count + 1
		tot = tot + i
avg = tot / count
print(avg)
		