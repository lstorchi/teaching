d = {"k1":1, "k2":"valore", 3:"val3", "quattro":4}
for x in d.itervalues():
    print x
print " "
for x in d.iterkeys():
    print x
print " "
for x in d.iteritems():
    print x
    print x[0], x[1]
