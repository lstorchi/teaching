import matplotlib.pyplot
import numpy 

numbers = numpy.random.randn(1000)
matplotlib.pyplot.hist(numbers)
matplotlib.pyplot.title("Istogramma")
matplotlib.pyplot.xlabel("Valore")
matplotlib.pyplot.ylabel("Freq.")
matplotlib.pyplot.show()
