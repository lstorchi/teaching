import random 
import numpy
import math 
import sys

import matplotlib.pyplot as plt

DIM = 0

if len(sys.argv) != 2:
    print("usage: ", sys.argv[0] , " NUM ")
    exit(1)
else:
    DIM = int(sys.argv[1])

p_rect_count = 0 
n_rect_count = 0

xmin = 2.0
xmax = 5.0 
ymin = -1.0
ymax = 1.0

plt.clf()

xv = []
yv = []
xvo = []
yvo = []

for i in range(0,DIM): 

   x = random.uniform(xmin, math.pi) 
   y = random.uniform(0.0, ymax) 

   if (y <= math.sin(x)):
     p_rect_count = p_rect_count + 1 
     xv.append(x)
     yv.append(y)
   else:
     xvo.append(x)
     yvo.append(y)

for i in range(0,DIM): 

   x = random.uniform(math.pi, xmax) 
   y = random.uniform(ymin, 0.0) 

   if (y >= math.sin(x)):
     n_rect_count = n_rect_count + 1 
     xv.append(x)
     yv.append(y)
   else:
     xvo.append(x)
     yvo.append(y)

p = 1.0 * ((math.pi - xmin) * ( float(p_rect_count) / float(DIM) ))
n = -1.0 * ((xmax - math.pi) * ( float(n_rect_count) / float(DIM) ))

print(p + n) 

plt.plot(xv, yv, ',')
plt.plot(xvo, yvo, '.')
x = numpy.linspace(2.0, 5.0, 1000) 
f = numpy.sin(x)
#print x
#print f
plt.plot(x, f, 'red', linestyle='--', linewidth=2, label='$sin(x)$')
legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

axes = plt.gca()
axes.set_xlim([2.0, 5.0]) 
axes.set_ylim([-1.5, 1.5])

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
