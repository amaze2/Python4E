count = 0
sum = 0
while True:
	number = input("Please enter a number: ")
	if number == "done":
		break
	else:
		try:
			fnumber = float(number)
		except:
			print("Invalid Input.")
			continue
		count = count + 1
		sum = sum + fnumber
		avg = sum / count			
print(sum, count, avg)