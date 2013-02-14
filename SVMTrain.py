#****************************************************************************
#This script gives data.dat files including features and also labales to    *
#svmtrain and make the models for different sets of parameters.             *
# (for now only train)                                                      *
#Author:Nima Behzad                                                         *
#11-11-12                                                                   *
#****************************************************************************
import subprocess

InPath = '/home/sm/Untitled/Untitled Folder/TrainFiltered_scaled.dat'
OutPath = '/home/sm/Workspace/trashModels/Scaled/13-12-12/TrashBin_'
SVMCheckData = '/home/sm/Nima/libsvm-3.12/tools/checkdata.py'
SVMScale = '/home/sm/Nima/libsvm-3.12/svm-scale'
SVMTrainPath = '/home/sm/Nima/libsvm-3.12/svm-train'
wNeg = '1'

#weights = [10, 100, 1000]
for j in range(-2,3):
	for i in range(1,7):
		#print weights[i]
		wPos = str(pow(10,i))
		G = str(pow(10,j))
		print wPos,G
		#OutPath1 = OutPath + str(weights[i]) + '.model'
		OutPath1 = OutPath + 'G' + G + 'wPos' + wPos + 'wNeg' + wNeg + '.model'
		print OutPath1
		#subprocess.call([SVMCheckData,InPath])
#TODO:
#1.fix this line to save the result of scale
#2.Add running grid.py to find best parameters
#		subprocess.call([SVMScale,'-l',' 0',InPath,' >','scaled.dat'])#InPath[:-4]+'_scaled.dat'])
#Gausian with gamma 0.1 and c 100 and first class weight to 10, suppose that first class is positive class. 
		subprocess.call([SVMTrainPath,'-t','2','-g',G,'-c','100','-w1',wPos,'-w-1',wNeg,'-b','1',InPath,OutPath1])
