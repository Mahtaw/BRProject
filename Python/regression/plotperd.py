# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:19:23 2016

@author: mggm6
"""

import matplotlib.pyplot as plt
import pandas as pd
import sklearn.preprocessing as preprocessing
import numpy as np
import matplotlib.pyplot as plt


direc='R:\\Research\\GeologicalScience\\sdm\\DatasummaryMG\\Neural Network\\'
	

data = pd.read_csv(direc+'y_test.csv')
df=pd.DataFrame.from_dict(data)
a=range(len(df))

df["difference"]=df["Predicted"]-df["y_test"]
df["midpoint"]=df["y_test"]+0.5*df["difference"]
fig=plt.figure(figsize=(60, 2))
ax=fig.add_subplot(111)

'''
plt.plot(a,Ypredict,'or')
plt.plot(a,y_test,'vb')
'''
bars=ax.errorbar(a,df["midpoint"],yerr=0.5*df["difference"], fmt='none',elinewidth = 4, color='K', ecolor='K')
ax.set_xlim((0,441))
