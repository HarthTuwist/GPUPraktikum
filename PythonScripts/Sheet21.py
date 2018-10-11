# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:21:45 2017

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#size = np.multiply(np.arange(1,11), np.power(2, 27))
xaxis = np.array((1,2,4,8,16))

#measuring results
#100 measurements: results = np.array(((0.000473266,0.00046473,0.000472649,0.000464746,0.000465371,0.000478553,0.813487,0.643209,0.620037,0.619706,0.812109),(0.000472133,0.000472544,0.000468757,0.000472752,0.000473639,0.402638,0.34957,0.324487,0.314772,0.316899,0.421756),(0.000468914,0.000476126,0.000466874,0.000467728,0.272603,0.216486,0.189532,0.178994,0.175887,0.197283,0.453904),(0.000467647,0.000476342,0.000472132,0.199292,0.177136,0.165277,0.163886,0.165169,0.282236,0.609466,0.761853),(0.000475753,0.000479518,0.266441,0.166782,0.165275,0.162971,0.163125,0.205851,0.568744,0.908647,1.04003)))
#results = np.array(((0.329924,0.179536,0.130495,0.107444,0.0948588,0.076294,0.0676096,0.0633691,0.0616029,0.0614042,0.0771857),(0.133017,0.0874623,0.0669848,0.0552857,0.0483843,0.0386757,0.0340198,0.0319055,0.0311179,0.0312344,0.0391806),(0.10717,0.0571094,0.0394554,0.0309145,0.0260419,0.0205718,0.018055,0.0170859,0.0168647,0.018826,0.0487728),(0.106688,0.0527563,0.0274827,0.0195667,0.0175308,0.0164568,0.0163786,0.0165093,0.0250266,0.061248,0.0771122),(0.106265,0.0525372,0.0266447,0.0167697,0.0165755,0.0163679,0.0164003,0.0206229,0.0536795,0.0916356,0.104462)))
#results = np.array(((2.61298,1.62405,1.26052,1.06436,0.948205,0.766116,0.675969,0.633381,0.616054,0.614004,0.772724),(1.33132,0.875688,0.670655,0.553391,0.484313,0.387616,0.340744,0.320671,0.313601,0.3143,0.392688),(1.07165,0.572085,0.395681,0.309968,0.26124,0.206754,0.181675,0.171837,0.169632,0.189333,0.462107),(1.06681,0.527508,0.275172,0.196316,0.176246,0.165549,0.164862,0.166231,0.255454,0.613058,0.771539),(1.06248,0.525368,0.266423,0.168685,0.166804,0.164644,0.164967,0.205683,0.545491,0.913257,1.04219)))
results = np.array(((2.59131,1.72532,1.59229,1.44865,1.56928,1.89392,1.83155,1.84455,1.92018,1.91735,2.7309),(1.32592,1.1292,1.08335,1.07292,1.13287,1.10131,1.11489,1.185,1.19958,1.57796,1.63481),(1.0715,1.05544,1.04161,1.04953,1.05011,1.0508,1.05497,1.06246,1.08153,1.11216,1.10565),(1.06683,1.04887,1.0444,1.04869,1.05262,1.05419,1.05843,1.04797,1.0576,1.05035,1.07182),(1.06241,1.0458,1.04738,1.0505,1.05206,1.05196,1.05295,1.05556,1.05418,1.05715,1.06257)))
#results[np.where(results < 0.002)] = 1

#divide by 10 because we measured 10 times
results = np.divide(results, 100)

#divide by the size
resgbs= np.divide(np.power(2,30), results);
resgbs = resgbs * 2 #Durchsatz means one write, one read
resgbs= np.divide(resgbs, 1e9)

#is this really right? I doubt that
#resgbs= np.divide(resgbs, np.transpose(np.tile(xaxis, (11, 1))))

#resgbs[np.where(resgbs < 5000)] = 223000
#resgbs[np.where(resgbs > 5000)] = 0
maxLines = 6# max lines per subplot
sbpltNbmr = (np.floor(np.shape(resgbs)[1] / maxLines) + 1).astype(int)
rubbish, sbplts = plt.subplots(sbpltNbmr)
for plotNumber in range(0, sbpltNbmr):
    for i in range(0, maxLines):#(np.shape(resgbs)[1]):
        accessedGraph = i + maxLines * plotNumber
        if np.shape(resgbs)[1] > accessedGraph:
            sbplts[plotNumber].plot(xaxis, resgbs[:, accessedGraph], label = "I = " + str(2 ** accessedGraph))
            sbplts[plotNumber].scatter(xaxis, resgbs[:, accessedGraph])
#plt.axis.Tick
    sbplts[plotNumber].grid()
    sbplts[plotNumber].legend(bbox_to_anchor=(1.05,1), loc = 2)

plt.xlabel("sizeof(T)")
plt.ylabel("Datendurchsatz in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')
