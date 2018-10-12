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
plt.plot(xaxis, d2dgbs, color="c")
"""
#Gesamtgroesse = numBlocks*block_len*AccessSize
accessSize = np.array((1,2,4,8,16))
#totalSize1 = np.multiply(accessSize, 16384 * 1) #array with sizes depending on the accesSizes
#totalSize1024 = np.multiply(accessSize, 16384 * 1024)
blockLengths = np.power(4, np.arange(0,6))
totalSize = 16384 * np.multiply(np.transpose(np.tile(accessSize, (6,1))), np.tile(blockLengths, (5,1)))
#totalSize = np.multiply(np.tile(accessSize, (6,1)), np.transpose(np.tile(blockLengths, (5,1))))
#block_len1 = np.divide(np.array((0.000462126, 0.000464966, 0.000475576, 0.000503736, 0.000757214)), 10) #array with times per total run
#block_len1024 = np.divide(np.array((0.00331364, 0.00424626, 0.00821059 , 0.025891, 0.117192)), 10)

results=  np.array(((0.000453178,0.000442783,0.000442801,0.000445851,0.00088275,0.00330547),(0.00044168,0.000444989,0.00044535,0.000449576,0.00105659,0.00395122), (0.00044579,0.000443296,0.000445445,0.000547235,0.00180319,0.00683818), (0.000443806,0.000454328,0.00047691,0.000962273,0.00347359,0.0135615), (0.000444981,0.000447401,0.000546688,0.00179575,0.00681933,0.026879)))
results = results /10
resgbs = np.divide(totalSize,results)
resgbs = resgbs / 1e9
xaxis = accessSize

sbpltNbmr = 1
rubbish, sbplts = plt.subplots(sbpltNbmr)
for plotNumber in range(0, 1):
    for N in range(0, np.shape(results)[1]):#
    
        
       if results[plotNumber, 0] <= 10e30: 
            sbplts.plot(xaxis, resgbs[:,N], label = "BlockSize = " + str(blockLengths[N]))
            sbplts.scatter(xaxis, resgbs[:,N])#, s = 2)
#plt.axis.Tick
    sbplts.grid()
    sbplts.legend(bbox_to_anchor=(1.05,1), loc = 2)
plt.xlabel("sizeof(T) in Bytes")
plt.ylabel("Kopierrate in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')


#yaxis1 = np.divide(np.divide(totalSize1, block_len1), 10e9)
#yaxis2 = np.divide(np.divide(totalSize1024, block_len1024), 10e9)
#plt.plot(xaxis, yaxis1, color="r")
#plt.plot(xaxis, yaxis2, color="g")