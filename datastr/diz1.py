d = {"k1":1, "k2":"valore", 3:"val3"}
print d[3], d["k1"]
d["quattro"] = 4
print d 
if d.has_key("quattro"):
    print "chiave presente"
if not d.has_key(4):
    print "chiave non presente"
