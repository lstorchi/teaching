import matplotlib.pyplot
import numpy
import math

f = open("numbers.txt", "r")

values = []
i = 0
for l in f:
  i += 1
  valori = l.split()
  if len(valori) == 2:
    values.append(float(valori[0]))
    values.append(float(valori[1]))
  else:
    print("error while reading line: ", i)

m = numpy.mean(values)
s = numpy.std(values)

matplotlib.pyplot.hist(values)
matplotlib.pyplot.title("Istogramma")
matplotlib.pyplot.xlabel("Valore")
matplotlib.pyplot.ylabel("Freq.")

for v in values:
  matplotlib.pyplot.plot(v, 100.0, color = 'green', marker = '.')

matplotlib.pyplot.plot(m, 100.0, color = 'red', marker = 'H')
matplotlib.pyplot.plot(m-2.0*s, 100.0, color = 'red', marker = 'H')
matplotlib.pyplot.plot(m+2.0*s, 100.0, color = 'red', marker = 'H')

matplotlib.pyplot.show()

