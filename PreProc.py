#**************************************************************************
#Gets input path which should contain pcd files for pointcluds with type  *
#pointxyzrgb. and run PreProc on all of them saves the results in separate* 
#folder for each pointclouds.                                             *
#Author:Nima Behzad                                                       *
#09-11-12                                                                 *
#**************************************************************************

import os,shutil,subprocess
#files = glob.iglob(os.path.join(source_dir,"*.ext"))

for root, dirs, files in os.walk('.'):
	for file in files:
		if file[-4:].lower() == '.pcd':
			filepath = os.path.join(root,file)
			dirname = os.path.splitext(file)[0]			
			print dirname
			if not os.path.exists(os.path.join(root,dirname)):
				os.makedirs(os.path.join(root,dirname))
			shutil.copy(filepath,os.path.join(root,dirname))
			subprocess.call(["/home/sm/ros_workspace/FDetect/bin/PreProc","1",filepath,root+"/"+dirname+"/"+dirname+"_transfered"+".pcd",root+"/"+dirname+"/"+dirname+"_normal"+".pcd",root+"/"+dirname+"/"+dirname+"_TFP"+".pcd",root+"/"+dirname+"/"+dirname+"_Converted"+".pcd"])
