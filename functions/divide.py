def divide (vals, d = 2.0):
  res = []
  for v in vals:
    res.append(v / d)

  return res  

vals = [1.0, 3.5, 5.6, 7.8]
print vals
print divide(vals)
print divide(vals, 3.0)
