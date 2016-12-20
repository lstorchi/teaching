str = "Hello, World!"
index = str.find("ll")
if index >= 0:
  print "a ", index, " trovato ", str[index]

res = str.split(" ")
idx = 0
for r in res:
    idx += 1
    print idx , " - ", r

for i in range(0,len(str)):
    print str[i]
