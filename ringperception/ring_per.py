import pybel
import sys 
import re
import os

if (len(sys.argv)) == 2:
  filename = sys.argv[1]
else:
  print("usage :", sys.argv[0] , " smifile")
  exit(1)

filep = open(filename, "r")

i = 1
for line in filep:
  p = re.compile(r'\s+')
  line = p.sub(' ', line)
  line = line.lstrip()
  line = line.rstrip()

  line.replace(' ','')

  print("Molecule number : ", i)

  mol = pybel.readstring( "smi", line)
  ringn = 1
  for ring in mol.OBMol.GetSSSR():
    print(ringn , " --> ", ring.IsAromatic(), ring.Size())
    ringn = ringn + 1
    for a in mol.atoms:
      if (ring.IsMember(a.OBAtom)):
        print("  ", a.idx)

  mol.make3D(forcefield='mmff94', steps=50)

  outfname = str(i)+".sdf"
  if os.path.exists(outfname):
    os.remove(outfname)

  mol.write('sdf', outfname)

  i = i + 1
