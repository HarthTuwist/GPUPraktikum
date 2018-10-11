# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt

xaxis = np.array([0,1,2,3,4,5,6])
#yaxis = np.array([1.51553,8.9233e-05,0.000648203,0.0061845,0.0581663,0.578622,5.76415])
yaxis = np.array([3.1724e-05,8.0355e-05,0.000623906,0.00599389,0.0571372,0.569171,5.69988])

expAry = np.power(10, xaxis)
yaxis = np.divide(yaxis, expAry)

plt.plot(xaxis, yaxis)
plt.scatter(xaxis, yaxis)

