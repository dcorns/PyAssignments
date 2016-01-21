fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	ln = line.rstrip().split()
	for item in ln:
		if item not in lst: lst.append(item)
lst.sort()	
print lst