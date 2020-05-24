import sys

filename = ""
if len(sys.argv) != 2:
  print("usage: ", sys.argv[0], " filein") 
  exit(1)
else:
  filename = sys.argv[1] 

f = open (filename, "w")

lista = ["linea1", "linea2", "linea3"]
for l in lista:
    print(l, file=f)

f.close()

