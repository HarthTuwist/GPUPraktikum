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
xaxis = (np.arange(32) +1 )* 32
#xaxis = np.power(2, np.arange(11))

#measuring results
results =np.array(((41.9012,20.9765,14.0422,10.5396,8.46065,7.07197,6.07753,5.3143,4.74055,4.28515,3.91154,3.59364,3.39334,3.40073,3.38661,3.37863,3.41644,3.39384,3.38886,3.38618,3.42056,3.3933,3.38649,3.38493,3.4116,3.39153,3.38907,3.38787,3.40982,3.38689,3.39268,3.38823),(20.9267,10.5246,7.04566,5.29589,4.24627,3.55007,3.39581,3.391,3.42539,3.38826,3.38577,3.38628,3.40099,3.38769,3.39137,3.39049,3.39919,3.39577,3.39579,3.39607,3.39849,3.40059,3.39768,3.4007,3.39849,3.40238,3.40119,3.40638,3.40652,3.4062,3.40708,3.40974),(14.0072,7.04841,4.70668,3.54248,3.4295,3.41072,3.39747,3.40805,3.39872,3.38904,3.38711,3.38821,3.39091,3.39408,3.39431,3.3942,3.4,3.40142,3.40115,3.40317,3.40156,3.40612,3.40188,3.40368,3.405,3.40563,3.40427,3.40391,3.40793,3.40685,3.40649,3.40848),(10.5129,5.29567,3.53999,3.43318,3.41281,3.41741,3.38698,3.39622,3.39229,3.39612,3.39212,3.39387,3.39357,3.39777,3.39878,3.39875,3.40135,3.40269,3.40233,3.40312,3.40202,3.39949,3.404,3.40359,3.40374,3.40539,3.40463,3.40843,3.40913,3.40263,3.40191,3.41482),(8.42264,4.2363,3.42484,3.41698,3.39821,3.39032,3.38963,3.39499,3.39724,3.39982,3.39333,3.39756,3.40225,3.39714,3.39907,3.39784,3.40093,3.40209,3.40279,3.40417,3.40276,3.40144,3.40177,3.40054,3.40156,3.40033,3.39953,3.40269,3.40111,3.40009,3.40325,3.4063),(7.02838,3.5333,3.49945,3.42959,3.39562,3.38853,3.39257,3.40203,3.39938,3.40213,3.39923,3.39857,3.39849,3.39766,3.39872,3.39753,3.40287,3.40249,3.39977,3.39973,3.40415,3.39912,3.40106,3.40245,3.4013,3.40678,3.4045,3.40486,3.41108,3.40375,3.40469,3.41081),(6.03406,3.39489,3.39738,3.45055,3.39564,3.38928,3.39109,3.39867,3.40309,3.40198,3.39827,3.39715,3.39975,3.39992,3.40062,3.39718,3.39981,3.40315,3.39834,3.39876,3.40177,3.4002,3.40369,3.40483,3.40343,3.40252,3.40391,3.40331,3.40139,3.40192,3.40039,3.39887),(5.28627,3.38559,3.46065,3.43531,3.4033,3.39654,3.39792,3.40828,3.3991,3.40431,3.39853,3.39886,3.40301,3.39885,3.39928,3.40557,3.40051,3.40134,3.40255,3.40288,3.40394,3.40302,3.40357,3.4014,3.40265,3.4003,3.3984,3.39787,3.3973,3.39395,3.39925,3.42379)))
#divide by 10 because we measured 10 times
results = np.divide(results, 10)

#divide by the size
resgbs= np.divide(np.power(2,29), results);

resgbs= np.divide(resgbs, 1e9)

sbpltNbmr = 2
rubbish, sbplts = plt.subplots(sbpltNbmr)
plotNumber = 0
for lines in range(0, np.shape(results)[0]):

    sbplts[plotNumber].plot(xaxis, resgbs[lines,:], label = "L = " + str((2 ** 3) * 16))
    sbplts[plotNumber].scatter(xaxis, resgbs[lines,:], s = 2)
        #plt.axis.Tick
    sbplts[plotNumber].grid()
    sbplts[plotNumber].legend(bbox_to_anchor=(1.05,1), loc = 2)
    sbplts[plotNumber].set_title("N =" + str((2 ** plotNumber) * 8))
plt.xlabel("used j: I = 10^j")
plt.ylabel("Datendurchsatz in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')
