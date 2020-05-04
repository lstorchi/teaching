def opera (vals, d = 2.0, c = "/"):
  res = []
  for v in vals:
    if c == "/":
      res.append(v / d)
    elif c == "*":
      res.append(v * d)
    elif c == "+":
      res.append(v + d)
    elif c == "-":
      res.append(v - d) 

  return res  

vals = [1.0, 3.5, 5.6, 7.8]
print(vals)
print(opera(vals))
print(opera(vals, 3.0))
print(opera(vals, c = "+"))
