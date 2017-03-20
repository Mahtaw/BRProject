# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import os
import shutil


def avgRuns(numOfRuns,path):
    def avg(lis):
        out=np.zeros(lis[0].shape)
        for i in lis:
            out=out+i
        out=out/len(lis)
        return out

    brklist=[]
    porolist=[]
    for j in range(numOfRuns):
        j=j+1
        pth=path+str(j)+'\\'
        poropath=pth+'avgporo'+str(j)+'.csv'
        brkpath=pth+'brk'+str(j)+'.csv'
        brklist.append(np.loadtxt(brkpath,delimiter=','))
        porolist.append(np.loadtxt(poropath,delimiter=','))
    avgbrk=avg(brklist)
    avgporo=avg(porolist)
    return avgbrk,avgporo
        
        
rootpath='E:\\new run\\'
otherpaths=['73mg\\','5050mg\\','90%10% mg\\']

for i in otherpaths:
    path=rootpath+i+'50&20@'
    avgbrk,avgporo=avgRuns(5,path)
    newpath=path+'avg\\'
    if os.path.exists(newpath):
        shutil.rmtree(newpath)
    os.mkdir(newpath)
    np.savetxt(newpath+'brk.csv',avgbrk,delimiter=',')
    np.savetxt(newpath+'poro.csv',avgporo,delimiter=',')
        
        
