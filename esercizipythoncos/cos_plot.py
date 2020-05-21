import numpy
import math 
import sys

import matplotlib.pyplot as plt

DIM = 1000

if len(sys.argv) == 2:
    DIM = int(sys.argv[1])

xmin = -5.0
xmax = 5.0 
ymin = -1.5
ymax = 1.5

plt.clf()

x = numpy.linspace(-5.0, 5.0, DIM) 
f = numpy.cos(x)
plt.plot(x, f, 'red', linestyle='--', linewidth=2, label='$cos(x)$')
legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

axes = plt.gca()
axes.set_xlim([xmin, xmax]) 
axes.set_ylim([ymin, ymax])

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
