# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:57:53 2016

@author: mggm6
"""
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from matplotlib.mlab import griddata
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def importData():
	direc='R:\\Research\\GeologicalScience\\sdm\\DatasummaryMG\\'
	return pd.read_csv(direc+'train.csv'),pd.read_csv(direc+'test.csv')

	
	
if __name__=='__main__':
	data,datatest=importData()
	#%%
	data_X_train=np.array([data['pH'],data['MajorAnisotropy'], data['MinAnisotropy']]).transpose()
	datatest_X_test=np.array([datatest['pH'],datatest['MajorAnisotropy'], datatest['MinAnisotropy']]).transpose()
	#%%
	data_Y_train=np.array(data['poriosity_change']).reshape((2644,1))
	datatest_Y_test=np.array(datatest['poriosity_change']).reshape((882,1))

	#%%
	# Create linear regression object
	poly=PolynomialFeatures(degree=2)
	regr=linear_model.LinearRegression()
	polyxtrain=poly.fit_transform(data_X_train)
	polyxtest=poly.fit_transform(datatest_X_test)


	# Train the model using the training sets
	regr.fit(polyxtrain,data_Y_train)

	# The coefficients
	print('Coefficients: \n', regr.coef_)
	# The mean squared error
	print("Mean squared error: %.2f"
		  % np.mean((regr.predict(polyxtest) - datatest_Y_test) ** 2))
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.2f' % regr.score(polyxtest, datatest_Y_test))

	save={"Variance Score":regr.score(polyxtest, datatest_Y_test),"Mean Squared Error":np.mean((regr.predict(polyxtest) - datatest_Y_test) ** 2),
		  "Coefficients":regr.coef_  }
	#%%



	def plotPrediction(x1min,x1max,x2min,x2max,regrobject,polyobject):
		size=50
		x1=np.linspace(x1min,x1max,num=size) #Create evenly spaced vectors of length 10 that span from the minimum to the maximum of the x data
		x2=np.linspace(x2min,x2max,num=size)
		x1grid,x2grid=np.meshgrid(x1,x2) #create grids of the x data
		allpossiblecombos=np.vstack((x1grid.flatten(),x2grid.flatten())).transpose() #create a 2d array where each row is a set of possible x values. this is fit to be given to the polynomial object
		predictions1d=regrobject.predict(polyobject.fit_transform(allpossiblecombos)) #perform the polynomial transform on the xdata and get the predictions for those x values
		predictions=predictions1d.reshape(x1grid.shape) #shape the predictions to fit in a plot with the two xdata grids
		return x1grid,x2grid,predictions #return all arrays needed to plot a surface.
		
			
	# Plot outputs
	fig=plt.figure()
	ax=fig.add_subplot(1,1,1,projection='3d')
	ax.set_xlabel('pH')
	ax.set_ylabel('MagnesitePercentageInitial')
	ax.set_zlabel("Porosity Change")
	ax.scatter(datatest_X_test[:,0],datatest_X_test[:,1], datatest_Y_test,alpha=.5)
	#ax.scatter(datatest_X_test[:,0],datatest_X_test[:,1],regr.predict(polyxtest),c='r',marker='^')
	#PH,MG=np.meshgrid(np.unique(datatest_X_test[:,0]),np.unique(datatest_X_test[:,1]))
	#newxarr=np.array()
	X,Y,Z=plotPrediction(4,8,10,100,regr,poly)
	ax.plot_surface(X,Y,Z,alpha=.1)
	#ax.plot(datatest_X_test, regr.predict(datatest_X_test), color='blue',linewidth=3)
	plt.show()



