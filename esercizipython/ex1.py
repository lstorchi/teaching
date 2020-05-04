
N = 10
sum = 0.0

for i in range(0,N):
    val = input ("inserisci il numero %d "%(i+1))
    sum = sum + float(val)

print("la somma: ", sum)
print("valore medio: ", sum/N)
