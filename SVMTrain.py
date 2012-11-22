#****************************************************************************
#This script gives data.dat files including features and also labales to    *
#svmtrain and make the models for different sets of parameters.             *
# (for now only train)                                                      *
#Author:Nima Behzad                                                         *
#11-11-12                                                                   *
#****************************************************************************
import subprocess

InPath = '/home/sm/Desktop/test/Experiments/room_518_partial1/room_518_partial1_data.dat'
OutPath = '/home/sm/Desktop/test/Experiments/room_518_partial1/room_518_partial1.model'
SVMCheckData = '/home/sm/Nima/libsvm-3.12/tools/checkdata.py'
SVMScale = '/home/sm/Nima/libsvm-3.12/svm-scale'
SVMTrainPath = '/home/sm/Nima/libsvm-3.12/svm-train'

subprocess.call([SVMCheckData,InPath])
#TODO:
#1.fix this line to save the result of scale
#2.Add running grid.py to find best parameters
subprocess.call([SVMScale,'-l',' 0',InPath,' >','scaled.dat'])#InPath[:-4]+'_scaled.dat'])
#Gausian with gamma 0.1 and c 100 and first class weight to 10, suppose that first class is positive class. 
subprocess.call([SVMTrainPath,'-t','2','-g','0.1','-c','100','-w1','1','-w-1','1','-b','1',InPath,OutPath])
