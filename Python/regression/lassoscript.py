# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:21:22 2016

@author: mggm6
"""

from sklearn.linear_model import LassoCV
#import matplotlib.pyplot as plt
import usefulFuncs as uf
from sklearn.preprocessing import scale


train,test=uf.importData()


xVariables=train[['MajorAnisotropy','MinAnisotropy','MagnesitePercentageInitial.1','pH','kratio']]#select out variables that we are interested in
yVariable=train['poriosity_change']

transformedX,colNames=uf.xTransform(xVariables)
standardizedX=scale(transformedX)

regr=LassoCV()
regr.fit(standardizedX,yVariable)
display=[i for i in zip(colNames,regr.coef_) if i[1]!=0.0]
print(display)     
print(regr.score(scale(uf.xTransform(test[['MajorAnisotropy','MinAnisotropy','MagnesitePercentageInitial.1','pH','kratio']])[0]),test['poriosity_change']))

'''
def lasso_regression(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    lassoreg = Lasso(alpha=alpha,normalize=True, max_iter=1e5)
    lassoreg.fit(data[predictors],data['y'])
    y_pred = lassoreg.predict(data[predictors])
    
    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g'%alpha)
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([lassoreg.intercept_])
    ret.extend(lassoreg.coef_)
    return ret
'''