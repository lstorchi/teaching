def divido(a, b):
    return a/b

def moltiplico(a, b):
    return a * b

def sommo (a, b):
    return a + b

def sottraggo():
    return a - b

# un semplice dizionario
operazioni = {"/" : divido,
              "*" : moltiplico,
              "+" : sommo,
              "-" : sottraggo,
}

def opera (vals, d = 2.0, c = "/"):
  res = []
  for v in vals:
    res.append(operazioni[c] (v, d))

  return res  

vals = [1.0, 3.5, 5.6, 7.8]
print vals
print opera(vals)
print opera(vals, 3.0)
print opera(vals, c = "+")
