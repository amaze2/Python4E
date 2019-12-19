hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
hours = float(hours)
rate = float(rate)
if hours > 40:
	overtime = hours - 40
	pay = (40*rate) + (overtime*(rate*1.5))
else:
	pay = hours*rate
print(pay)