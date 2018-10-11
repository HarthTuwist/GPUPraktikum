# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
rcParams['figure.figsize'] = 5, 5

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
numBlocks = np.array((32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384))
#totalSize1 = np.dot(accessSize, numBlocks * 1) #array with sizes depending on the accesSizes
#totalSize1024 = np.dot(accessSize, numBlocks * 1024)
   
totalSize1024 = np.zeros((5,10))
for (x, y), value in np.ndenumerate(totalSize1024):
    totalSize1024[x][y] = accessSize[x] * numBlocks[y] * 1024
"""
times = np.zeros((5,11))

times[0] = np.array((0.000148054,0.000154983,0.000158668, 0.000175769,0.000221834,0.000288023 , 0.000538769,0.000935001,0.00172326,0.00330358,0.00647236))#aS1
times[1] = np.array((0.00014796,0.000156454, 0.000167627, 0.000193294 ,0.000247077 , 0.000401594, 0.000660154, 0.00116968,0.00219719,0.00425112,0.00836844))#aS2
times[2] = np.array((0.000159579, 0.000171137,0.000200504,0.000257173, 0.000402172,  0.000656695,0.00115895, 0.00217414,  0.00418656, 0.00822026,0.0163053 ))#aS4
times[3] = np.array((0.000213623, 0.000271261, 0.000367512, 0.000584533, 0.000985216, 0.00178811, 0.00339213, 0.00659264, 0.0130237, 0.0258882 , 0.0518186    ))#aS8
times[4] = np.array((0.000512666, 0.000743661, 0.00121172, 0.00214874 , 0.00404213, 0.00772189,0.0151328, 0.0299671, 0.0565415, 0.109793, 0.20229))#aS16
"""
times =  np.array(((0.00014233,0.000141748,0.000140168,0.000143296,0.000158667), (0.000143754,0.000145616,0.000146594,0.000150223,0.000167784), (0.000152531,0.000154444,0.000155942,0.000172384,0.000338324), (0.000170832,0.000166274,0.000176519,0.000339114,0.000543758), (0.000206828,0.000211553,0.000341971,0.000556664,0.00096732), (0.000278124,0.00036625,0.000546852,0.000962933,0.00179367), (0.000524152,0.000607413,0.000971686,0.00181332,0.00347511), (0.000926988,0.00108775,0.00181247,0.00348628,0.00681969), (0.00171538,0.00203641,0.00348611,0.00682667,0.0134795), (0.0032976,0.00391989,0.00682842,0.0135269,0.0268189)))
times = np.transpose(times)
times = np.divide(times, 10)# because we measure 10 times

resgbs = np.divide(totalSize1024, times) / 1e9

#plt.plot(accessSize, numBlocks, zs = durchsatze)

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

yaxis = np.repeat(numBlocks,accessSize.size) 
xaxis = np.tile(accessSize, (1,numBlocks.size)).flatten()

#ax.plot_surface(xaxis, yaxis, durchsatze.flatten())

ax.scatter(xaxis, yaxis, durchsatze.flatten('F'), c='r', marker='o')
ax.plot_wireframe(xaxis, yaxis, durchsatze.flatten('F'))

#ax.view_init(elev=0, azim=90)

ax.set_xlabel('copy Size in By')
ax.set_ylabel('numBlocks')
ax.set_zlabel('Speed in GB/s')

plt.show()
"""
xaxis = accessSize#np.tile(accessSize, (1,numBlocks.size)).flatten()
maxLines = 6# max lines per subplot
sbpltNbmr = (np.floor(np.shape(resgbs)[1] / maxLines) + 1).astype(int)
rubbish, sbplts = plt.subplots(sbpltNbmr)
for plotNumber in range(0, sbpltNbmr):
    for i in range(0, maxLines):#(np.shape(resgbs)[1]):
        accessedGraph = i + maxLines * plotNumber
        if np.shape(resgbs)[1] > accessedGraph:
            sbplts[plotNumber].plot(xaxis, resgbs[:, accessedGraph], label = "numBlocks = " + str(numBlocks[accessedGraph]))
            sbplts[plotNumber].scatter(xaxis, resgbs[:, accessedGraph])
#plt.axis.Tick
    sbplts[plotNumber].grid()
    sbplts[plotNumber].legend(bbox_to_anchor=(1.05,1), loc = 2)

plt.xlabel("sizeof(T)")
plt.ylabel("Kopierrate in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')

rcParams['figure.figsize'] = 5, 3