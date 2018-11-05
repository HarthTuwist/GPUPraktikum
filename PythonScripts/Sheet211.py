# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['figure.figsize'] = 5, 6

#size = np.multiply(np.arange(1,11), np.power(2, 27))
xaxis = np.arange(11)
#xaxis = np.power(2, np.arange(11))

#measuring results
results = np.array((((0.106746,0.104668,0.10489,0.104837,0.104933,0.104948,0.105276,0.105029,0.106205,0.105911,0.105713),(0.106244,0.104583,0.104786,0.105092,0.105237,0.105229,0.105367,0.105552,0.105461,0.105755,0.106068),(0.106256,0.105768,0.105913,0.106022,0.105694,0.105389,0.105414,0.105654,0.105482,0.105533,0.106199)),((0.106261,0.104576,0.105031,0.105048,0.104926,0.104953,0.105273,0.105,0.106289,0.106128,0.105502),(0.106242,0.104583,0.104753,0.105066,0.105237,0.105225,0.105316,0.105581,0.105448,0.10574,0.106256),(0.106167,0.106138,0.105825,0.105865,0.10579,0.105358,0.105404,0.10574,0.105479,0.105511,0.10626)),((0.10627,0.104576,0.105084,0.105033,0.104914,0.104934,0.105245,0.105047,0.106413,0.106007,0.105549),(0.106182,0.10464,0.104792,0.105036,0.105185,0.105134,0.105326,0.105586,0.105435,0.10549,0.1064),(10e42,10e42,10e42,10e42,10e42,10e42,10e42,10e42,10e42,10e42,10e42))))
#divide by 10 because we measured 10 times
results = np.divide(results, 10)

#divide by the size
resgbs= np.divide(np.power(2,30), results);

resgbs= np.divide(resgbs, 1e9)
""" #no more Datendurchsatz
resgbs= resgbs*2

yticks = np.arange(200, 207)
"""

yticks = np.arange(100, 104)

sbpltNbmr = np.shape(results)[0]
rubbish, sbplts = plt.subplots(sbpltNbmr)
for plotNumber in range(0, sbpltNbmr):
    for l in range(0, np.shape(results)[1]):#
    
        
       if results[plotNumber, l, 0] <= 10e30: 
            sbplts[plotNumber].plot(xaxis, resgbs[plotNumber,l,:], label =str((2 ** l) * 16) + " Threads")
            sbplts[plotNumber].scatter(xaxis, resgbs[plotNumber,l,:], s = 2)
            sbplts[plotNumber].set_yticks(yticks)
#plt.axis.Tick
    sbplts[plotNumber].grid(which = 'major', alpha = 0.2)
    sbplts[plotNumber].legend(bbox_to_anchor=(1.05,1), loc = 2)
    sbplts[plotNumber].set_title(str((2 ** plotNumber) * 8) + " Subdomains")
    
for ax in sbplts.flat:
    ax.set(ylabel="Kopierrate in GB/s", xlabel="$\log_{10}$(Iterationen)")
#plt.xlabel("used j: I = 2^j")
#plt.ylabel("Datendurchsatz in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')
rcParams['figure.figsize'] = 5, 3