import random 
import math 

A =  [[0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0]]

B =  [[0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0]]

C =  [[0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0]]

for i in range(len(A)):
  for j in range(len(A[0])):
    A[i][j] = random.uniform(0.0, 1.0)

for i in range(len(A)):
  for j in range(len(A[0])):
    B[i][j] = random.uniform(0.0, 1.0)

for i in range(len(A)):
  for j in range(len(B[0])):
    for k in range(len(B)):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]

print "Matrix A"
for i in range(len(A)):
  print A[i]

print "Matrix B"
for i in range(len(B)):
  print B[i]

print "Matrix C"
for i in range(len(C)):
  print C[i]
