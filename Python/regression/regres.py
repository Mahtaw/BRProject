# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:18:04 2016

@author: mggm6
"""

from sklearn import linear_model
import matplotlib.pyplot as plt
import usefulFuncs as uf
import pandas as pd
import sklearn.preprocessing as preprocessing
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

direc='R:\\Research\\GeologicalScience\\sdm\\DatasummaryMG\\'
	
train = pd.read_csv(direc+'train.csv')
test = pd.read_csv(direc+'test.csv')

train,test=uf.importData()


 
X_train=train[['MajorAnisotropy','MinAnisotropy','pH','MagnesitePercentageInitial','MgPerm','kratio']]#select out variables that we are interested in\n",
y_train=train['poriosity_change']
   
X_test=test[['MajorAnisotropy','MinAnisotropy','pH','MagnesitePercentageInitial','MgPerm', 'kratio']]#select out variables that we are interested in\n",
y_test1=test['poriosity_change']


X_train,X_trainNames=uf.xTransform(X_train)
X_test,X_testNames=uf.xTransform(X_test)

print('start')
for i in range(X_test.shape[0]):
    for j in range(X_test.shape[1]):
        if X_test[i,j]>1.7e308 or X_test[i,j]<-1.7e308 or np.isnan(X_test[i,j]) or np.isinf(X_test[i,j]):
            print(i,j)



preproc = preprocessing.StandardScaler()
preproc = preproc.fit(X_train)
X_train = preproc.transform(X_train)
X_test = preproc.transform(X_test)
#LASSO
model = linear_model.LassoCV(fit_intercept=False,max_iter=100000)
model = model.fit(X_train, y_train)
score = model.score(X_test, y_test1)
lassocv_alpha = model.alpha_
print(score)
display=[i for i in zip(X_trainNames,model.coef_) if i[1]!=0.0]
print(display) 

Lresults=[i for i in range(len(model.coef_)) if model.coef_[i]!=0.0]
newxtrain= X_train[:,Lresults]
X_test_new= X_test[:,Lresults]

newxtest , newxvalidation, y_test, y_validation_new = train_test_split(X_test_new, y_test1, test_size=0.5, random_state=1)

#Linear using selected parameters
Model= linear_model.LinearRegression()
Model= Model.fit(newxtrain,y_train)
ScoreTrain= Model.score(newxtrain,y_train)
ScoreL= Model.score(newxtest,y_test)
print(ScoreL)
displayLinear=[i for i in zip(display,Model.coef_)]
print(displayLinear)

#real=pd.DataFrame(data=y_test, index= None,columns=newxtest)
#print (real)

Ypredict=Model.predict(newxtest)
a=range(len(newxtest))
dic={"y":y_test, "yPredict":Ypredict}
'''
for i in range(len(display)):
    dic[display[i][0]]=newxtest[:,i]
'''
df=pd.DataFrame.from_dict(dic)
df["difference"]=df["yPredict"]-df["y"]
df["midpoint"]=df["y"]+0.5*df["difference"]
fig=plt.figure(figsize=(60, 2))
ax=fig.add_subplot(111)

'''
plt.plot(a,Ypredict,'or')
plt.plot(a,y_test,'vb')
'''
bars=ax.errorbar(a,df["midpoint"],yerr=0.5*df["difference"],fmt='none',elinewidth = 4, color='K', ecolor='K')
ax.set_xlim((0,a[-1]+2))
'''
plt.plot(a,Ypredict,'or')
plt.plot(a,y_test,'ob')

R=rd.sample(range(len(y_test)),30)
indeXX=list (R)
for i in indeXX:
    x=newxtest[indeXX]
    y=y_test[indeXX]

dic={"index":R,"y":y, "yPredict":Ypredcit}
for i in range(len(display)):
    dic[display[i][0]]=x[:,i]
df=pd.DataFrame.from_dict(dic)

a=range(30)
plt.plot(a,Ypredcit,'or')
plt.plot(a,y,'ob')
plt.plot(y,Ypredcit)
plt.show()

df = pd.DataFrame(columns=['x','y','Ypredict'], index=list (R), dtype=int)
x = pd.Series(x, index=list (R), dtype=int)
y = pd.Series(y, index=list (R), dtype=int)
z = pd.Series(Ypredcit, index=list (R), dtype=int)
df.loc['x']=x; df.loc['y']=y; df.loc['z']=z
'''