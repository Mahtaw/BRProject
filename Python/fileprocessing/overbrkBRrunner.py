# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:58:31 2017

@author: mggm6
"""

import glob,subprocess, os
import sys


folders=glob.glob(r'R:\Research\GeologicalScience\sdm\mahta\out-flow1-0.005\*') #Creates a list of all paths matching the pattern
flowRate=1 #Sets the number for flowrate that will be passed to Matlab


cmd="addpath('R:\Research\GeologicalScience\sdm\Source\Matlab');" #adds the path where matlab can find its code
badPaths=[] #a list of paths that are not valid
for i in folders:
    if os.path.exists(i+'\\area13.out'): #checks of the .out files have been made
        #if not os.path.exists(i+'\\brk.csv'): #if the brk has already been made then skip
            cmd+="overbrkBR(false,%f,%s);"%(flowRate,"'"+i+"'") #Adds the matlab command to the cmd string
    else:
        badPaths.append(i)
print("Badpaths: ",badPaths)
#cmd+='quit;'
print('starting matlab')
process=subprocess.Popen(["matlab", '-wait', "-r", cmd]) #Begins a new matlab process.
