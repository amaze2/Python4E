def computegrade(score):
	if grade < 0 or grade > 1:
		print("Error. Bye.")
	else:
		if grade >= 0.9:
			print("A")
		elif grade >= 0.8 and grade < 0.9:
			print("B")
		elif grade >= 0.7 and grade < 0.8:
			print("C")
		elif grade >= 0.6 and grade < 0.7:
			print("D")
		else:
			print("F")
			
grade = float(input("Please enter grade between 0.0 and 1.0: "))
computegrade(grade)