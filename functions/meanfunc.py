def calcola (vals):
  sum = 0.0
  for v in vals:
    sum += v
  
  return sum/len(vals)

valori = [1.1, 4.0, 5.0, 9.5, 5.6]
m = calcola(valori)
print("valore medio: ", m)  
