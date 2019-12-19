count = dict()
words = []

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
          words = line.split()
          time = words[5].split(":")
          count[time[0]] = count.get(time[0], 0) + 1

list = list()
for k,v in count.items():
	list.append((k,v))

list.sort()

for k,v in list:
	print(k,v)
