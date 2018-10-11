# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

size = np.multiply(np.arange(1,11), np.power(2, 27))
xaxis = np.divide(size, np.power(2,20))

#measuring results
h2d = np.array((0.522401, 1.04203, 1.56239, 2.0828, 2.60292, 3.12315, 3.64429, 4.16328, 4.68356, 5.20365))
d2h = np.array((0.669908, 1.32441, 1.98528, 2.63957, 3.29884, 3.96111, 4.62645, 5.28329, 5.9406, 6.59862))
h2h = np.array((0.251437, 0.501636, 0.751511, 1.01015, 1.25621, 1.5098, 1.75567, 2.00754, 2.25642, 2.50627))
d2d = np.array((0.0137916, 0.0273404, 0.0409656, 0.054548, 0.068159, 0.0817084, 0.0953037, 0.108856, 0.122488, 0.136068))


#new values
results = np.array(((0.266827,0.468877,0.305779,0.013794),(0.53583,0.940338,0.613911,0.0273378),(0.809261,1.40699,0.926505,0.0409744),(1.0594,1.88486,1.23211,0.0548467),(1.33223,2.34364,1.53339,0.068174),(1.61055,2.81789,1.83945,0.0817386),(1.87981,3.28485,2.14292,0.0953119),(2.14897,3.74736,2.44596,0.109048),(2.42013,4.21982,2.75402,0.122502),(2.68973,4.6856,3.06258,0.136178)))
#measurement on capture02
results = np.array(((0.473996,0.512101,0.293204,0.0137225),(0.868516,1.02189,0.585187,0.0273173),(1.31178,1.52589,0.89376,0.0408283),(1.74319,2.03589,1.16543,0.0562266),(2.18793,2.54527,1.47331,0.0693935),(2.61561,3.05257,1.74586,0.0842971),(3.06506,3.56161,2.05009,0.0990662),(3.4955,4.07499,2.34988,0.113727),(3.93969,4.57494,2.64146,0.128634),(4.39246,5.0987,2.92765,0.145409)))


h2d = results[:,0]
d2h = results[:,1]
h2h = results[:,2]
d2d = results[:,3]


#divide by 10 because we measured 10 times
h2d = np.divide(h2d, 10)
d2h= np.divide(d2h, 10)
h2h= np.divide(h2h, 10)
d2d= np.divide(d2d, 10)

#divide by the size
h2dgbs= np.divide(size, h2d)
d2hgbs= np.divide(size, d2h)
h2hgbs= np.divide(size, h2h)
d2dgbs= np.divide(size, d2d)

h2dgbs= np.divide(h2dgbs, 1e9)
d2hgbs= np.divide(d2hgbs, 1e9)
h2hgbs= np.divide(h2hgbs, 1e9)
d2dgbs= np.divide(d2dgbs, 1e9)


plt.plot(xaxis, h2dgbs, color="r", label = "H2D") 
plt.plot(xaxis, d2hgbs, color="g", label = "D2H")
plt.plot(xaxis, h2hgbs, color="b", label = "H2H")
#plt.plot(xaxis, d2dgbs, color="c", label = "D2D")

plt.scatter(xaxis, h2dgbs) 
plt.scatter(xaxis, d2hgbs)
plt.scatter(xaxis, h2hgbs)
#plt.scatter(xaxis, d2dgbs)

#plt.axis.Tick
plt.xlabel("Groesse in MiBit")
plt.ylabel("Datenkopierrate in GB/s")
plt.grid()
plt.legend(bbox_to_anchor=(1.05,1), loc = 2)
plt.savefig('fig.svg', format='svg', bbox_inches='tight')
