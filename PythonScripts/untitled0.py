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

plt.plot(xaxis, h2dgbs, color="r", label = "H2D") 
plt.plot(xaxis, d2hgbs, color="g", label = "D2H")
plt.plot(xaxis, h2hgbs, color="b", label = "H2H")
plt.plot(xaxis, d2dgbs, color="c", label = "D2D")

plt.scatter(xaxis, h2dgbs) 
plt.scatter(xaxis, d2hgbs)
plt.scatter(xaxis, h2hgbs)
plt.scatter(xaxis, d2dgbs)

#plt.axis.Tick
plt.xlabel("Groesse in MiBit")
plt.ylabel("Datendurchsatz in GB/s")
plt.grid()
plt.legend(bbox_to_anchor=(1.05,1), loc = 2)
plt.savefig('fig.svg', format='svg', bbox_inches='tight')