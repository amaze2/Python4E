def chop(list):
	del list[0]
	del list [-1]
	return None
	
def middle(list):
	del list[0]
	del list [-1]
	return list
	
lst=[1,2,3,4,5]



chop(lst)
print(lst)

middle(lst)