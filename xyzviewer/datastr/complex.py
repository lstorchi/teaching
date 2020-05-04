a = 2 + 3j
b = 4 - 1j

print(a)
print(a.real, " ", a.imag)
print(b)
print(b.real, " ", b.imag)

c = a * b
print(type(c), " valore ", c)

if type(c) == complex:
    print("c e\' un numero complesso")

