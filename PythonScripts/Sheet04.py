# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt

size = np.multiply(np.arange(1,11), np.power(2, 27))
xaxis = np.divide(size, np.power(2,20))
#yaxis = np.array([1.51553,8.9233e-05,0.000648203,0.0061845,0.0581663,0.578622,5.76415])
#yaxis = np.array([3.1724e-05,8.0355e-05,0.000623906,0.00599389,0.0571372,0.569171,5.69988])

#expAry = np.power(10, xaxis)
#yaxis = np.divide(yaxis, expAry)

#plt.plot(xaxis, yaxis)

h2d = np.array((0.522401, 1.04203, 1.56239, 2.0828, 2.60292, 3.12315, 3.64429, 4.16328, 4.68356, 5.20365))
d2h = np.array((0.669908, 1.32441, 1.98528, 2.63957, 3.29884, 3.96111, 4.62645, 5.28329, 5.9406, 6.59862))
h2h = np.array((0.251437, 0.501636, 0.751511, 1.01015, 1.25621, 1.5098, 1.75567, 2.00754, 2.25642, 2.50627))
d2d = np.array((0.0137916, 0.027341, 0.0409656, 0.054548, 0.068159, 0.0817084, 0.0953037, 0.108856, 0.122488, 0.136068))
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

h2dgbs= np.divide(h2dgbs, 10e9)
d2hgbs= np.divide(d2hgbs, 10e9)
h2hgbs= np.divide(h2hgbs, 10e9)
d2dgbs= np.divide(d2dgbs, 10e9)

plt.plot(xaxis, h2dgbs, color="r") 
plt.plot(xaxis, d2hgbs, color="g")
plt.plot(xaxis, h2hgbs, color="b")
plt.plot(xaxis, d2dgbs, color="c")