fname = raw_input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
line_count = 0
fn = open(fname);
for line in fn:
	if not line.startswith('From '): continue
	print line.split()[1]
	line_count = line_count + 1
print 'There were', line_count, 'lines in the file with From as the first word'