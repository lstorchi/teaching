import random 
import math 
import sys

DIM = 0

if len(sys.argv) != 2:
    print "usage: ", sys.argv[0] , " NUM "
    exit(1)
else:
    DIM = int(sys.argv[1])

rect_count = 0 

xmin = 2.0
xmax = 5.0 
ymin = -1.0
ymax = 1.0

for i in range(0,DIM): 

   x = random.uniform(xmin, xmax) 
   y = random.uniform(ymin, ymax) 

   if x < math.pi :
     if ((y <= math.sin(x)) and (y >= 0.0)):
       rect_count = rect_count + 1 
   elif x >= math.pi :
     if ((y >= math.sin(x)) and (y <= 0.0)):
         rect_count = rect_count - 1

p = (xmax - xmin) * (ymax - ymin) * (float(rect_count) / float(DIM))

print p
