#****************************************************************************
#This script  gets two path for input pointclouds and normals               *
#And an output path to save results of feature extract. (for now only train)*
#Author:Nima Behzad                                                         *
#9-11-12                                                                    *
#****************************************************************************
import os,shutil,subprocess,glob

FeatExtPath ='/home/nims/Desktop/experiment environment/ContextModel-master/bin/FD'
InPath = '/home/nims/Desktop/experiment environment/PreProc'
OutPath = '/home/nims/Desktop/experiment environment/Trash_experiment_22-11-12/'
ObjClassName = 'TrashBin'
l = len(ObjClassName+'_annotated.pcd')
for root, dirs, files in os.walk(InPath):
	for file in files:
		if file[-13:].lower() == 'annotated.pcd':
					  
			filepath = os.path.join(root,file)
                        print filepath
#			filebase = os.path.splitext(file)[1]
#			filebase = filepath[:-14]
			filebase = file[:-(l+1)]			
			print filebase
			if not os.path.exists(os.path.join(OutPath,filebase)):
				os.makedirs(os.path.join(OutPath,filebase))
			subprocess.call([FeatExtPath,"1",filepath,filepath[:-(l+1)]+"_normal.pcd",OutPath+filebase+"/"+filebase+"_IP.dat",OutPath+filebase+"/"+filebase+"_data.dat",OutPath+filebase+"/"+filebase+"_label.dat",OutPath+ObjClassName+"_train.dat",OutPath+ObjClassName+"_labels.dat",OutPath+filebase+"/"+filebase+"_downsampled.pcd"])
