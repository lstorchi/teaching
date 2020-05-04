import pandas
import numpy
import sys
import re

filename = ""
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("usage: ", sys.argv[0], " filename.txt")
    exit(1)

df = pandas.read_excel(filename)
cn = df.columns

print("CN: ", cn)

values = numpy.asarray(df[cn[0]].values)
print(numpy.mean(values), " ", numpy.std(values)) 
