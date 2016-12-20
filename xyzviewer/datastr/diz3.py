d = {"k1":1, "k2":"valore", 3:"val3", "quattro":4}
del d["k1"]
for x in d.iteritems():
    print x
d.clear()
print len(d)
for x in d.iteritems():
    print x
