# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:51:26 2017

@author: mggm6
"""

#Unfinished. don't Use
import glob,os,subprocess,shutil
class MatlabProcessor:
    def __init__(self,homeDir='R:\\Research\\GeologicalScience\\sdm\\mahta\\',matlabSearchPath=r'R:\Research\GeologicalScience\sdm\Source\Matlab'):
        self.homeDir=homeDir
        self.cmd=None
        self.matlabSearchPath=matlabSearchPath
        
    def getFileList(self,pattern):
        self.fileList=glob.glob(os.path.join(self.homedir,pattern))
        
    def runMatlab(self,string):
        if self.cmd=None:
            print('no command has been entered')
            return
        out=("addpath('%s');"%self.matlabSearchPath)+self.cmd+'quit;'
        self.process=subprocess.Popen(["matlab", '-wait', "-r", out])
    
    def copyFromTemplate(self,templatePath):
        for i in self.fileList:
            #create folders
            shutil.copytree(os.path.join(self.homeDir,templatePath),i)
            shutil.copy(direc+'grdcloutputfiles\\'+runName+'\\'+runName+'@%d.GRDECL'%(i),fulldir)