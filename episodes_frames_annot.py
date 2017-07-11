import os

rootdir = 'episodes_frames/'

currDir = os.getcwd()

annotDir = currDir + '/episodes_frames_annot/'

if not os.path.exists(annotDir):
	os.makedirs(annotDir)

for fold in os.listdir(rootdir):
	if 'DS_Store' in fold:
		continue

	fileAnnot = open(annotDir + '/' + fold + '.txt', 'w')

	for files in os.listdir(rootdir + fold):
		if 'DS_Store' in files:
			continue
		fileAnnot.write('episodes_frames/' + fold + '/' + files + '\n')
