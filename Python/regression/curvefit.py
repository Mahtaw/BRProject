# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:39:10 2016

@author: mggm6
"""

from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
trainx=train['pH']
trainy=train.poriosity_change
testx=test.pH
testy=test.poriosity_change

def poly(x,A,B,C):
    y=A+B*x+C*x**2
    return y
    
def exponential(x,A,B):
    y=A*np.log(x)+B
    return y

def getR2(func,fits,xdata,ydata):
    yfunc=func(xdata,*fits)
    residuals=ydata-yfunc
    ss_res=np.sum(residuals**2)
    ss_tot=np.sum((ydata-np.mean(ydata))**2)
    return 1-ss_res/ss_tot


functions=[poly,exponential]
for fitfunc in functions:
    fits,covariance=curve_fit(fitfunc,trainx,trainy)
    print(fits)
    print(getR2(fitfunc,fits,testx,testy))
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(testx,testy)
    x=np.linspace(4,8)
    ax.plot(x,fitfunc(x,*fits))
    #plt.pause(.1)
plt.show()
