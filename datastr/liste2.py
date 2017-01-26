a = [1, 3.5, -6.0, 5]
a.append(46)
print a
print "rimuove l\'ultimo elemento: ", a.pop()
a.append(46)
i = len(a) - 1
print "rimuove l\'elemento ", i, " ", a.pop(i)
a.sort()
print a

print (1 in a)
print a.index(-6.0) 
