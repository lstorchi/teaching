import numpy
import math

########################################################

def mean_stdev_welford (values):
  
  m = 0.0 

  if len(values) == 1:
    m = values[0] 
 
  s = 0.0

  # vedi il Knuth "Art of Computer Programming"
  if len(values) >= 1:
    moldm = values[0]
    mnewm = values[0]
    molds = 0.0
    mnews = 0.0
    i = 0

    for i in range(1, len(values)):
      x = values[i]
      mnewm = moldm + (x - moldm)/(i+1)
      mnews = molds + (x - moldm)*(x - mnewm)
    
      moldm = mnewm 
      molds = mnews
  
    s = math.sqrt(mnews/(i+1))
    m = mnewm

  return m, s

########################################################

f = open("numbers.txt", "r")

values = []
i = 0
for l in f:
  i += 1
  valori = l.split()
  if len(valori) == 2:
    values.append(float(valori[0]))
    values.append(float(valori[1]))
  else:
    print("error while reading line: ", i)

m, s = mean_stdev_welford (values)
print("media: ", m, " ", numpy.mean(values))
print("stdev: ", s, " ", numpy.std(values)) # diviso n = len(values)

# classico con rischio di overflow 
if len(values) >= 1:
  m = 0.0
  s = 0.0

  for v in values:
    m += v
  m = m / len(values)
  
  for v in values:
    s += (v-m)**2
  s = s/len(values)
  s = math.sqrt(s)

  print("media: ", m)
  print("stdev: ", s)

f.close()

