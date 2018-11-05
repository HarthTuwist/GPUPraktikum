# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt
"""
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
plt.plot(xaxis, d2dgbs, color="c")"""
#asdf = np.array((0.00821161, 0.0146268, 0.0323531, 0.0571496, 0.0764847))
#nonrefvalues asdf = np.array((0.00685628,0.0143599,0.0286455,0.0576069,0.058636))

######### data type = 4 values


# =  np.array((0.00179724,0.00366934,0.00724247,0.0145073,0.0147632,0.017998,0.0263649))
#arraysize = 8192 * 512 *  4
#xaxis = np.array((1,2,4,8,16, 32, 64))



#####data type = 16 values
#asdf = np.array((0.00177678,0.00370368,0.00378415,0.00464311,0.00622071,0.00835998,0.0135893))
#arraysize = 4096 * 256 *  16
#xaxis = np.array((1,2,4,8,16, 32, 64))


###values 
"""
asdf= np.array((0.000980812,0.0019283,0.00373975,0.00382389,0.00467476,0.00626902,0.00839288))
arraysize = 4096 * 256 *  8
xaxis = np.array((1,2,4,8,16, 32, 64))
"""

"""
asdf =np.array((0.000555964,0.00101991,0.00190063,0.00374345,0.00383317,0.00460381,0.00623002,0.0083957,0.0133928))
arraysize = 4096 * 256 *  4
xaxis = np.array((1,2,4,8,16, 32, 64, 128, 256))
"""



"""
asdf = np.array((0.000568752,0.000701398,0.00119612,0.00227781,0.00442838,0.00876888,0.00898949,0.0108378,0.0144795))
arraysize = 8192 * 256 *  1
xaxis = np.array((1,2,4,8,16, 32, 64, 128, 256))
"""


asdf = np.array((0.000313963,0.000346841,0.00057045,0.00102672,0.00105015,0.00133986,0.00177956,0.00221614,0.00329035,0.00318467,0.00345528))
arraysize = 2048 * 128 *  4
xaxis = np.array((1,2,4,8,16, 32, 64, 128, 256, 512, 1024))


"""
asdf = np.array((0.000551359,0.00103171,0.00105536,0.00129003,0.0016892,0.00221098,0.003239090, .00324708,0.00345248))
arraysize = 2048 * 128 *  16
xaxis = np.array((1,2,4,8,16, 32, 64, 128, 256))
"""

asdf = np.divide(asdf, 10)

plt.figure()

plt.plot(xaxis,  np.divide(np.divide(arraysize, asdf), 1e9))
plt.scatter(xaxis,  np.divide(np.divide(arraysize, asdf), 1e9))

plt.xlabel("Stride in Elementen")
plt.ylabel("Kopierrate in GB/s")
#plt.xticks(xaxis)


plt.grid()
#plt.xticks(np.arange(0, 1000, step=50))
#plt.xticks([0.2, 0.4, 0.6, 0.8, 1.])
plt.savefig('fig.svg', format='svg', bbox_inches='tight')