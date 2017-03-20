# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:11:50 2017

@author: mggm6
"""
import pandas as pd
import glob

direc='R:\\Research\\GeologicalScience\\sdm\\mahta\\out-flow1-0.005\\'
flowRate=1


runs=glob.glob(direc+'*\\brk.csv')
rundata={}
for foldernum,brkfile in enumerate(runs):
    print('Running %d of %d'%(foldernum,len(runs)))
  
    brk=pd.read_csv(brkfile,sep=',',names=['time','br'])
    c0=brk['br'].iloc[0]
    brk['PV']=brk['time']*60*flowRate/140
    srchnums=[c0*0.1,c0*0.01,c0*0.001]
    finaldata=pd.DataFrame()
    #Save the final dataframe for one breakthrough
    for i in srchnums:
        bestrow=brk.ix[(brk.br-i).abs().argsort()[0]]
        bestrow['target']=i
        finaldata=finaldata.append(bestrow)
    
    rundata[brkfile.split('\\')[-2]]=finaldata        
