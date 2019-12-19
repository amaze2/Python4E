
minimum = None
maximum = None
while True:
	number = input("Please enter a number: ")
	if number == "done":
		break
	else:
		try:
			number = float(number)
		except:
			print("Invalid Input.")
			continue
	if minimum is None or number < minimum:
		minimum = number 
	if maximum is None or number > maximum:
		maximum = number

print(minimum, maximum)
