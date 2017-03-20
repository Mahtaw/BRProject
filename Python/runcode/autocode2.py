import shutil as sh
import glob
import subprocess

runName='17576-11-10-1'
direc='R:\\Research\\GeologicalScience\\sdm\\mahta\\'
flowRate=25
copyFiles=True

MajorA,MinorA=runName.split('-')[2:]
MajorA=int(MajorA)
MinorA=int(MinorA)


if copyFiles:
    _=glob.glob(direc+runName+'@*')
    if len(_)>1:
        print(_)
        raise NameError("More than one folder for this run exists!")
        
    
    for i in range(1,11):
        print("Copying %d"%i)
        fulldir=direc+runName+'@%d'%i
        sh.copytree(direc+'Flow25-0.005',fulldir)
        #Folders have now been created
        sh.copy(direc+'grdcloutputfiles\\'+runName+'\\'+runName+'@%d.GRDECL'%(i),fulldir)
    print("Done Copying")

cmd="addpath('R:\Research\GeologicalScience\sdm\Source\Matlab');"
for i in range(1,11):
    fulldir=direc+runName+'@%d'%i
    cmd+="runcrunchflow(%f,%f,%f,%s);"%(flowRate,MajorA,MinorA,"'"+fulldir+"'")
cmd+='quit;'
print('starting matlab')
process=subprocess.Popen(["matlab", '-wait', "-r", cmd])

