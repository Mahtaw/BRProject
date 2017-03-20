# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:39:38 2016

@author: Mahta
"""

from glob import glob
import numpy as np
import csv
import sys
import os

#rootpath='E:\\1st\\'#mat files\\'
#paths=glob(rootpath+'*\\*\\*[0-9]\\data.csv')
#rootpath='E:\\new run\\'
#paths+=glob(rootpath+'*\\*[0-9]\\data.csv')

rootpath=r'R:\Research\GeologicalScience\sdm\mahta\out-flow1-0.005'
paths=glob(os.path.join(rootpath,'*[0-9]\\data.csv'))
print(paths)
input('press enter to continue')

'''
badpaths=[]
for i in paths:
    if not os.path.isfile(i+'rate10.out'):
        badpaths.append(i)
'''


firstTime=True
for path in paths:
    if firstTime:
        data=np.genfromtxt(path,delimiter=',')
        firstTime=False
    else:
        newdata=np.genfromtxt(path,delimiter=',')
        data=np.vstack((data,newdata))
print(data.shape)
input('Press enter!: ')

header=['Filename',"Mean Pr","STDev Pr",'Flowrate','MajorAnisotropy','MinAnisotropy','Porosity','OveralRate','AveragePorosity']
f=open(os.path.join(rootpath,'stackeroutput.csv'),'w',newline='')
csvwriter=csv.writer(f)
csvwriter.writerow(header)
for i,path in enumerate(paths):
    l=path.split('\\')[-3:-1]
    fileName=l[0]+'/'+l[1]
    meanPr,stdevPr=l[1].split('-')[:2]
    newrow=[fileName,meanPr,stdevPr]+list(data[i,:])
    csvwriter.writerow(newrow)
f.close()

