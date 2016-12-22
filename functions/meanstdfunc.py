import math

def calcola (vals):
  n = float(len(vals))

  m = 0.0
  for v in vals:
    m += v
  m = m / n
  
  s = 0.0
  for v in vals:
    s = (v-m)**2  
  s = s / n
  s = math.sqrt(s) 

  return m, s

valori = [1.1, 4.0, 5.0, 9.5, 5.6]
m, s = calcola(valori)
print "valore medio: ", m , " stdev: ", s
