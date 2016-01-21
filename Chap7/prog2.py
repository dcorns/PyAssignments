fname = raw_input("Enter file name: ")
fh = open(fname)
line_count = 0
line_sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line_count = line_count + 1
    line_sum = line_sum + float(line.rstrip().split(': ')[-1])
print "Average spam confidence:", (line_sum / line_count)
