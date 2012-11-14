#**************************************************************************
#Gets input path which should contain pcd files for pointcluds with type  *
#pointxyzrgb. and run PreProc on all of them saves the results in separate* 
#folder for each pointclouds.                                             *
#Author:Nima Behzad                                                       *
#09-11-12                                                                 *
#**************************************************************************

import os,shutil,subprocess
FDetectPath = "/home/nims/Desktop/experiment environment/ContextModel-master"
CloudsPath = "/home/nims/Desktop/experiment environment/Clouds"
ResultPath = "/home/nims/Desktop/experiment environment/PreProc"
#files = glob.iglob(os.path.join(source_dir,"*.ext"))

for root, dirs, files in os.walk(CloudsPath):
	for file in files:
		if file[-4:].lower() == '.pcd':
			filepath = os.path.join(root,file)
			dirname = os.path.splitext(file)[0]			
			print dirname
			if not os.path.exists(os.path.join(ResultPath,dirname)):
				os.makedirs(os.path.join(ResultPath,dirname))
			shutil.copy(filepath,os.path.join(ResultPath,dirname))
			subprocess.call([FDetectPath+"/bin/PreProc","1",filepath,ResultPath+"/"+dirname+"/"+dirname+"_transfered"+".pcd",ResultPath+"/"+dirname+"/"+dirname+"_normal"+".pcd",ResultPath+"/"+dirname+"/"+dirname+"_TFP"+".pcd",ResultPath+"/"+dirname+"/"+dirname+"_Converted"+".pcd"])
