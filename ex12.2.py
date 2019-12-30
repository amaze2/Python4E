import socket

URL = input("Please enter the website address that you wish to retrieve: ")
try: 
	burl = URL.split("/")
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((burl[2], 80))
	cmd = ('GET ' + URL + ' HTTP/1.0\r\n\r\n').encode()
	mysock.send(cmd)

	while True:
		data = mysock.recv(512) 
		if len(data) < 1:
			break
		data = data.decode()
		data = data[:3000]
		print(data)
		print(len(data))

	mysock.close()

except:
	print("Your URL is improper.")