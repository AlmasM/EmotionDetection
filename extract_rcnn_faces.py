# provided rcnn txt file that has coordinates and confidence level,
# this code creates folders, organizes them and employs face_recognition
# package that is based on dlib library

# Note: code doesn't employ RCNN code to extract faces

import os
import cv2
from PIL import Image, ImageDraw
import face_recognition
import name_faces
from name_faces import face_recog_main



rootdir = '/Users/almas/Documents/Research/'

rcnn_files = rootdir + 'rcnn_files/'

face_recog = rootdir + "face_recog/"
assert os.path.isdir(face_recog)


extractedFaces = face_recog + 'rcnn_recog_faces/'
if not os.path.exists(extractedFaces):
	os.makedirs(extractedFaces)

# output file for check
outCheck = open(rcnn_files + 'output.txt', 'w')



def coordExtract(coord):
	number_float = map(float, coord.split())
	return number_float
	# return [x, y, h, w]


for fold in os.listdir(rcnn_files):
	if 'DS_Store' in fold:
		continue

	print fold
	outCheck.write(fold + '\n') 

	if fold.endswith('.txt'):
		fileEp = open(rcnn_files + fold, 'r')

		folderName = fold.strip('.txt')

		folderName = extractedFaces + folderName
		# folderName = ../Documents/Research/face_recog/rcnn_recog_faces/
		if not os.path.exists(folderName):
			os.makedirs(folderName)

		for line in fileEp:

			if 'ep' in line:
				picLoc = line.strip('\n')
				faceList = []

				faceCount = int(next(fileEp))
				
				t = 0
				while faceCount > t:
					faceList.append(next(fileEp).strip('\n'))
					t = t + 1

				
				imOriginal = rootdir + picLoc

				if os.path.isfile(imOriginal):
					image = Image.open(imOriginal)
				else:
					continue

				picName = os.path.basename(imOriginal)
				# imMod = folderName + '/' + picName


				outCheck.write(os.path.basename(imOriginal) + '\n')

				faceCoordList = []
				for count, coord in enumerate(faceList):
					x = coordExtract(coord)
					
					conf_tresh = x.pop()

					# update list x coords x[2], x[3] 
					x[0] = x[0] - 15
					x[1] = x[1] - 15 
					x[2] = x[0] + x[2] + 15
					x[3] = x[1] + x[3] + 15
					if x and conf_tresh >= 0.96:
						outCheck.write(str(x) + "\n")
						draw = ImageDraw.Draw(image)
						draw.rectangle(x)

						img_crop = image.crop(x)
						img_crop.save(folderName  + '/' + str(count) + '_' + os.path.basename(imOriginal))
						
					image.save(imOriginal)

				# if faceList:
				# 	break	
		
		face_recog_main(folderName)
				
	# break


