import random 
import math 

A =  [[0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0]]

for i in range(len(A)):
  for j in range(len(A[0])):
    A[i][j] = random.uniform(0.0, 1.0)

print("Matrix A")
print(A)
