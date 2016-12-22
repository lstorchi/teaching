import math

def solv (a, b, c):
  
  delta = math.pow(b, 2.0) - (4.0 * a * c)

  if (delta >= 0):

    tn = math.sqrt(delta)

    sol1 = ((-1.0 * b) + tn) / (2.0 * a)
    sol2 = ((-1.0 * b) - tn) / (2.0 * a)

    return sol1, sol2

  return "NAN", "NAN"
  

ai = input("insert a:") 
a = float(ai)

bi = input("insert b:")
b = float(bi)

ci = input("insert c:")
c = float(ci)

print "a = ", a, " b = ", b, " c = ", c

x1, x2 = solv (a, b, c)

if (x1 == "NAN") and (x2 == "NAN"):
  print "non ci sono soluzioni reali" 
else:
  print "soluzioni: ", x1, x2
