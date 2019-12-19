str = "X-DSPAM-Confidence:0.8475"
numstart = str.find(":")
number = str[numstart+1:]
fnumber = float(number)
print(fnumber)