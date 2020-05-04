import math

ai = eval(input("insert a:")) 
a = float(ai)

bi = eval(input("insert b:"))
b = float(bi)

ci = eval(input("insert c:"))
c = float(ci)

print("a = ", a, " b = ", b, " c = ", c)

delta = math.pow(b, 2.0) - (4.0 * a * c)

if (delta >= 0):

  tn = math.sqrt(delta)

  sol1 = ((-1.0 * b) + tn) / (2.0 * a)
  sol2 = ((-1.0 * b) - tn) / (2.0 * a)

  print(sol1, sol2)

else:

  print("No real solutions")
