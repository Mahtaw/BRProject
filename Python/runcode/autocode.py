import shutil as sh
import glob
import subprocess

runName='17576-112-100-100'


direc='R:\\Research\\GeologicalScience\\sdm\\mahta\\'

_=glob.glob(direc+runName+'@*')
if len(_)>1:
    print(_)
    raise NameError("More than one folder for this run exists!")
 

input("Please change the anisotropy values in the InputWriter file and press enter: ")

for i in range(1,11):
    print("Copying %d"%i)
    fulldir=direc+runName+'@%d'%i
    sh.copytree(direc+'t4 - Copy',fulldir)
    #Folders have now been created
    sh.copy(direc+'grdcloutputfiles\\'+runName+'\\'+runName+'@%d.GRDECL'%(i),fulldir)
print("Done Copying")

cmd=''
for i in range(1,11):
    fulldir=direc+runName+'@%d'%i
    cmd+="run('%s\\InputWriter.m');"%fulldir
cmd+='quit;'
print('starting matlab')
process=subprocess.Popen(["matlab", '-wait', "-r", cmd])
    


