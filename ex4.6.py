def computepay(x, y):
	try:
		hours = float(hours)
		rate = float(rate)
	except:
		hours = input("Please enter a number: ")
		rate = input("Please enter a number: ")
		hours = float(hours)
		rate = float(rate)
	
	if hours > 40:
		overtime = hours - 40
		pay = (40*rate) + (overtime*(rate*1.5))
	else:
		pay = hours*rate
	print(pay)
	
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
computepay(hours, rate)