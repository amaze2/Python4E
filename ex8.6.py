
number_list = []
while True:
	number = input("Please enter a number: ")
	if number == "done":
		break
	else:
		try:
			number = float(number)
			number_list.append(number)
		except:
			print("Invalid Input.")
			continue
maximum = max(number_list)
minimum = min(number_list)

print(minimum, maximum)