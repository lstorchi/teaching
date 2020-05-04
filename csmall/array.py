import random

N = 20

a = []
b = []

for i in range(N):
    a.append(random.randrange(1, 30))
    b.append(random.randrange(1, 30))

for i in range(N):
    print(("%3d %3d"%(a[i], b[i])))

s = 0.0
for i in range(10):
    s = s + float(a[i]*b[i])

print("")
print(("S = %.5e"%s))
