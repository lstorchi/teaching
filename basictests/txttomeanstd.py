import numpy
import sys
import re

filename = ""
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "usage: ", sys.argv[0], " filename.txt"
    exit(1)

values = []
fp = open(filename, "r")
for line in fp:
    p = re.compile(r'\s+')
    line = p.sub(' ', line)
    line = line.lstrip()
    line = line.rstrip()

    sline = line.split(' ')

    if len(sline) == 1:
        values.append(float(sline[0]))

print numpy.mean(values), " ", numpy.std(values) 

fp.close()
