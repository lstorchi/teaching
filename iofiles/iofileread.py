import sys

filename = ""

if len(sys.argv) != 2:
  print "usage: ", sys.argv[0], " filein" 
  exit(1)
else:
  filename = sys.argv[1] 

f = open (filename, "r")

l = f.readline()
print l 
lines = f.readlines()
print lines 

f.seek(0, 0) # offset primo parametro, whence 0 posizione assoluta, 
             # 1 posizione relativa rispetto all poszione attuale 
             # 2 poszione relativa alla fine del file
 
for l in f:
  print l

f.close()

