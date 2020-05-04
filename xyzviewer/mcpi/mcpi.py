import random 
import math 
import sys

DIM = 0

if len(sys.argv) != 2:
    print("usage: ", sys.argv[0] , " NUM ")
    exit(1)
else:
    DIM = int(sys.argv[1])

circle_count = 0 

for i in range(0,DIM): 

   x = random.uniform(0.0, 1.0) 
   y = random.uniform(0.0, 1.0) 

   if ((math.pow(x, 2.0) + math.pow(y, 2.0)) < 1.0): 
     circle_count = circle_count + 1 

pi = float(circle_count) / float(DIM) 

print(4.0 * pi) 
