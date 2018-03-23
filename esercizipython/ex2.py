import random

numtest = 10
a = random.randint(1, 20)
inp = a + 1

for i in range(0, numtest):
    inp = int(input("inserisci numero: " ))
    if inp < a:
        print "il numero inserito e' troppo piccolo "
    elif inp > a:
        print "il numero inserito e' troppo grande"
    else:
        print "bravo indovinato"
        break

