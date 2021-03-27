import pylab
import numpy

x=numpy.arange(-10,10,0.01)
y=numpy.zeros_like(x)
y[(x>-5.0)&(x<5.0)] = 1.0

pylab.subplot(2,1,1)
pylab.plot(x,y)
pylab.ylim([0,2])
fft=numpy.fft.fft(y)
freq=numpy.fft.fftfreq(len(x),d=0.01)
pylab.subplot(2,1,2)
pylab.plot(freq, numpy.abs(fft))

pylab.xlim([-3,3])
#pylab.ylim([-1,11000])
pylab.show()