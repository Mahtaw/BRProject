# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:57:53 2016

@author: mggm6
"""
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from matplotlib.mlab import griddata
#from sklearn.preprocessing import PolynomialFeatures


data=pd.read_csv('train.csv')
datatest=pd.read_csv('test.csv')

#%%
data_X_train=np.array([data['pH'],data['MagnesitePercentageInitial']]).transpose()
datatest_X_test=np.array([datatest['pH'],datatest['MagnesitePercentageInitial']]).transpose()
#%%
data_Y_train=np.array(data['poriosity_change']).reshape((2644,1))
datatest_Y_test=np.array(datatest['poriosity_change']).reshape((882,1))
'''

poly=PolynomialFeatures()
x_=poly.fit_transform(data_X_train)
predict_=poly.fit_transform(data_Y_train)
'''


#%%
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(data_X_train, data_Y_train)


# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(datatest_X_test) - datatest_Y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(datatest_X_test, datatest_Y_test))

#%%
# Plot outputs
fig=plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
ax.set_xlabel('pH')
ax.set_ylabel('MagnesitePercentageInitial')
ax.set_zlabel("Porosity Change")
ax.scatter(datatest_X_test[:,0],datatest_X_test[:,1], datatest_Y_test,alpha=.5)
ax.scatter(datatest_X_test[:,0],datatest_X_test[:,1],regr.predict(datatest_X_test),c='r',marker='^')
#ax.scatter(data_X_train,data_Y_train,color='r')
#ax.plot(datatest_X_test, regr.predict(datatest_X_test), color='blue',linewidth=3)
plt.show()


