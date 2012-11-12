#****************************************************************************
#This script  gets two path for input pointclouds and normals               *
#And an output path to save results of feature extract. (for now only train)*
#Author:Nima Behzad                                                         *
#9-11-12                                                                    *
#****************************************************************************
import os,shutil,subprocess,glob

InPath = '/home/sm/Desktop/test'
OutPath = '/home/sm/Desktop/test/Experiments/'

for root, dirs, files in os.walk(InPath):
	for file in files:
		if file[-13:].lower() == 'annotated.pcd':
					  
			filepath = os.path.join(root,file)
                        print filepath
#			filebase = os.path.splitext(file)[1]
#			filebase = filepath[:-14]
			filebase = file[:-14]			
			print filebase
			if not os.path.exists(os.path.join(OutPath,filebase)):
				os.makedirs(os.path.join(OutPath,filebase))
			subprocess.call(["/home/sm/ros_workspace/FDetect/bin/FD","1",filepath,filepath[:-14]+"_normal.pcd",OutPath+filebase+"/"+filebase+"_IP.dat",OutPath+filebase+"/"+filebase+"_data.dat",OutPath+filebase+"/"+filebase+"_label.dat"])