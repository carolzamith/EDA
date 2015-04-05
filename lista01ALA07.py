import pylab

__author__ = 'Carol'


t = [0.00016,0.00018,0.00034,0.00058,0.00188,0.00935,0.04835,0.29986]

c = [16,32,64,128,256,512,1024,2048]

pylab.plot(c,t)
pylab.xlabel('this is dimension')
pylab.ylabel('this is time')

pylab.title('Lista 1 - Exercicio 7')

pylab.show()