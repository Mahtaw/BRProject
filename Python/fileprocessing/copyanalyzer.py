# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 19:16:01 2016

@author: mggm6
"""

import glob,shutil,sys
import os

direc='R:\\Research\\GeologicalScience\\sdm\\ph6\\'

folders=glob.glob(direc+'91same\\*\\')

for i in folders:
    if not os.path.isdir(i):
        raise ValueError('OMG, Dont ruin your life!')
for i in folders:
    shutil.copy(direc+'InputTemplate.in',i)
