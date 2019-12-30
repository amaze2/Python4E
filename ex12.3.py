import urllib.request

URL = input("Please enter the website address that you with to retrieve: ")
try: 
	data = urllib.request.urlopen(URL)
	data = data.read()
	print(data[:3000])
	print(len(data))


except:
	print("Your URL is improper.")