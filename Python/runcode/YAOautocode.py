# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:34:16 2016

@author: mggm6
"""

import shutil as sh
import glob
import subprocess
import time

runNames=['55\\100&50']

direc='R:\\Research\\GeologicalScience\\sdm\\ph6\\'
#time.sleep(10*3600)
'''
for runName in runNames:
    cmd=''
    for i in range(1,11):
        fulldir=direc+runName+'@%d'%i
        #cmd+="run('%s\\InputWriter.m');"%fulldir
        cmd+="run('%s\\InputWriter.m');"%fulldir
    cmd+='quit;'
    print('starting matlab')
    process=subprocess.Popen(["matlab", '-wait', "-r", cmd])
    #if runNames!=runNames[-1]:
     #time.sleep(8*3600)

print ('done')
''''