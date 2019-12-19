count = 0
sum = 0

filename = input("Please enter the filename: ")
if filename == "na na boo boo":
	print("You have been punked!")
	quit()
else:
	fhand = open(filename)
	for line in fhand:
		if line.startswith("X-DSPAM-Confidence:"):
			numstart = line.find(":")
			number = line[numstart+1:]
			fnumber = float(number)
			count = count + 1
			sum = sum + fnumber
print(sum / count)