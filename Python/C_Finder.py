# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:11:50 2017

@author: mggm6
"""
import pandas as pd
import glob

direc='R:\\Research\\GeologicalScience\\sdm\\mahta\\'

runs=glob.glob(direc+'1*@*')
rundata={}
for foldernum,runfolder in enumerate(runs):
    print('Running %d of %d'%(foldernum,len(runs)))
    runnum=runfolder.split('\\')[-1]
    files=glob.glob(runfolder+'\\breakthrough*.out')    
    breakthroughdata={}
    for file in files:
        #file=r'R:\Research\GeologicalScience\sdm\mahta\17576-11-20-1@9\breakthrough99.out'
        brk=pd.read_csv(file,sep='   ',skiprows=2,names=['time','br'])
        c0=brk['br'].iloc[0]
        brk['PV']=brk['time']*60*5/140
        srchnums=[c0*0.1,c0*0.01,c0*0.001]
        finaldata=pd.DataFrame()
        #Save the final dataframe for one breakthrough
        for i in srchnums:
            bestrow=brk.ix[(brk.br-i).abs().argsort()[0]]
            bestrow['target']=i
            finaldata=finaldata.append(bestrow)
        breakthroughdata[file.split('\\')[-1][:-4]]=finaldata
    rundata[runnum]=breakthroughdata        
