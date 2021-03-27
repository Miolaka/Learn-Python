#The first example uses performance optimized numpy arrays to create a gauss curve and write data to both binary and formated files. Then we read both datasets from the last example and plot one over the other.
import numpy
import math
import pylab

var=1.0
x=numpy.arange(-10,10,0.001)

y=(1.0/(var*math.sqrt(2.0*math.pi)))*numpy.exp(-0.5*x*x/var**2)

x.tofile('gauss_binary.dat')
y.tofile('gauss_ascii.dat', sep='\n', format='%e')

x=numpy.fromfile('gauss_binary.dat', dtype=float)
y=numpy.fromfile('gauss_ascii.dat', sep='\n')

pylab.plot(x,y)
pylab.show()
#now editing with Linux