# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:18:45 2017

@author: mggm6
"""
import pickle
import pandas as pd

#imports csummary data as a dicionary
with open('R:\Research\GeologicalScience\sdm\mahta\out-flow1-0.005\Csummary.mah','rb') as f:
    csum=pickle.load(f)

df=pd.read_csv(r'R:\Research\GeologicalScience\sdm\yao\SummaryPh4&6&8.csv')
