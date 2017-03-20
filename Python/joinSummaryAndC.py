# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:36:07 2017

@author: mggm6
"""
import pickle
import pandas as pd
import os
import sys

def CtoRow(inData):
    a,b,c=[list(inData.iloc[0]),list(inData.iloc[1]),list(inData.iloc[2])]
    df=pd.DataFrame(data=[a+b+c],columns=['PV E-1','br E-1',
                    'targetC E-1','t E-1','PV E-2','br E-2',
                    'targetC E-2','t E-2','PV E-3','br E-3',
                    'targetC E-3','t E-3'])
    return df

rootpath=r'R:\Research\GeologicalScience\sdm\mahta\out-flow1-0.005'
Csum=pickle.load(open(os.path.join(rootpath,'Csummary.mah'),'rb'))
Sum=pd.read_csv(os.path.join(rootpath,'stackeroutput.csv'))

newRows=pd.DataFrame(columns=['PV E-1','br E-1',
                    'targetC E-1','t E-1','PV E-2','br E-2',
                    'targetC E-2','t E-2','PV E-3','br E-3',
                    'targetC E-3','t E-3'])
for i,row in Sum.iterrows():
    key=row['Filename'].split('/')[-1]
    C=Csum[key]
    C=CtoRow(C)
    C.index=[i]
    newRows=newRows.append(C)
final=pd.concat([Sum,newRows],axis=1)