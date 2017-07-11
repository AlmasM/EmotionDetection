from PIL import Image
import os
import re

rootdir = 'episodes_frames/'
newdir = 'episodes_frames_j/'

for fold in os.listdir(rootdir):
	if 'DS_Store' in fold:
		continue

	currDir = newdir + fold
	print currDir
	if not os.path.exists(currDir):
		os.makedirs(currDir)

	for files in os.listdir(rootdir + fold):
		if 'DS_Store' in files:
			continue

		im = Image.open(rootdir + fold + '/' + files)
		im.save((currDir + '/' + files).replace('.jpeg', '') + '.jpg')