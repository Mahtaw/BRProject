# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:17:40 2016

@author: Nick
"""

from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plotPrediction(x1data,x2data,regrobject,polyobject):
    x1=np.linspace(x1data.min(),x1data.max(),num=10) #Create evenly spaced vectors of length 10 that span from the minimum to the maximum of the x data
    x2=np.linspace(x2data.min(),x2data.max(),num=10)
    x1grid,x2grid=np.meshgrid(x1,x2) #create grids of the x data
    allpossiblecombos=np.vstack((x1grid.flatten(),x2grid.flatten())).transpose() #create a 2d array where each row is a set of possible x values. this is fit to be given to the polynomial object
    predictions1d=regrobject.predict(polyobject.fit_transform(allpossiblecombos)) #perform the polynomial transform on the xdata and get the predictions for those x values
    predictions=predictions1d.reshape(x1grid.shape) #shape the predictions to fit in a plot with the two xdata grids
    return x1grid,x2grid,predictions #return all arrays needed to plot a surface.
    

#Example
    
x1d=np.array([1,4,7,9])
x2d=np.array([.2,.3,.4,.2])
y=np.array([3,4,9,8])
xdata=np.vstack((x1d,x2d)).transpose()
regr=LinearRegression()
regr.fit(xdata,y)
X,Y,Z=plotPrediction(x1d,x2d,regr)

fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(X,Y,Z,alpha=.1)
ax.scatter(x1d,x2d,y)