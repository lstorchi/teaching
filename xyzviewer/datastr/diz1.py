d = {"k1":1, "k2":"valore", 3:"val3"}
print(d[3], d["k1"])
d["quattro"] = 4
print(d) 
if "quattro" in d:
    print("chiave presente")
if 4 not in d:
    print("chiave non presente")
