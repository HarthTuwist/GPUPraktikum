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
resultsd2hwritecomb = np.array(((41.9474,21.0309,14.0309,10.5513,8.45035,7.08607,6.08876,5.31453,4.73476,4.28554,3.91484,3.59785,3.3902,3.40156,3.38815,3.37863,3.41566,3.39318,3.38754,3.38801,3.42083,3.39246,3.38617,3.38673,3.40974,3.39274,3.38862,3.38805,3.41035,3.3877,3.39219,3.38759),(20.9818,10.5335,7.03512,5.29769,4.25629,3.5606,3.39599,3.39048,3.42612,3.38762,3.38574,3.38318,3.40131,3.38837,3.39036,3.38856,3.40144,3.39643,3.39616,3.3966,3.39987,3.40143,3.39897,3.4003,3.39865,3.40343,3.40121,3.40569,3.40786,3.40572,3.40678,3.41126),(14.0112,7.04101,4.70981,3.55148,3.4279,3.40671,3.40076,3.39791,3.40017,3.38978,3.38713,3.38797,3.39229,3.39422,3.39688,3.39677,3.40042,3.40205,3.40241,3.40276,3.40295,3.40693,3.40317,3.40648,3.40642,3.40841,3.40538,3.40441,3.41063,3.40885,3.4094,3.407),(10.5173,5.29651,3.54786,3.44469,3.41793,3.41623,3.39222,3.40306,3.39258,3.39587,3.39294,3.39357,3.3954,3.39762,3.39953,3.40015,3.40143,3.4025,3.40511,3.40314,3.40264,3.4001,3.40355,3.40495,3.40477,3.40421,3.40495,3.40981,3.40687,3.40524,3.40394,3.41703)))


###########TODO resultsh2dwritecomb



#results =
#divide by 10 because we measured 10 times
resultsd2hwritecomb = np.divide(resultsd2hwritecomb, 10)

#divide by the size
resgbs= np.divide(np.power(2,29), resultsd2hwritecomb);

resgbs= np.divide(resgbs, 1e9)

sbpltNbmr = 1
rubbish, sbplts = plt.subplots(sbpltNbmr)
plotNumber = 0
for lines in range(0, np.shape(resultsd2hwritecomb)[0]):

    sbplts.plot(xaxis, resgbs[lines,:], label = "M = " + str(lines + 1))
    sbplts.scatter(xaxis, resgbs[lines,:], s = 2)
        #plt.axis.Tick
    sbplts.grid(True)
    sbplts.legend(bbox_to_anchor=(1.05,1), loc = 2)
    sbplts.set_title("N =" + str((2 ** plotNumber) * 8))
plt.xlabel("used j: I = 10^j")
plt.ylabel("Datendurchsatz in GB/s")
plt.savefig('fig.svg', format='svg', bbox_inches='tight')
