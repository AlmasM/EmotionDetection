import face_recognition
import cv2
import os
from fuzzywuzzy import fuzz
from PIL import Image
from itertools import compress
from shutil import copyfile




# new file for images
newdir = '/Users/almas/Documents/Research/face_recog/'
outputCheck = open(newdir + 'output.txt', 'w')

path_initial = ""
pathNew = ""

char_known_faces = []
char_unknown_faces = []
char_names = []


# ndir = "new_images/"
# pathNew = os.path.join(newdir, ndir)
# try:
# 	os.makedirs(pathNew)
# except OSError:
# 	# print(path)
# 	pass

def get_chars(path):
	# print path
	image = face_recognition.load_image_file(path)	
	image_encoded = face_recognition.face_encodings(image)[0]
	char_known_faces.append(image_encoded)


def get_unknown_chars(path_un):
	path_initial = path_un
	unknown_image = face_recognition.load_image_file(path_un)
	face_locations = face_recognition.face_locations(unknown_image)	
	# print(face_locations)
	if face_locations != []:
		unknown_image_encoded = face_recognition.face_encodings(unknown_image, face_locations)
		detect_faces(unknown_image_encoded, path_un, face_locations, unknown_image)
	else:
		# #######
		# os.chdir(pathNew)
		face_image = unknown_image
		pil_image = Image.fromarray(face_image)
		pil_image.save(path_un)
		# cv2.imwrite(path_un.split("unknown_images/", 1)[1], pil_image)
		# cwd	

def detect_faces(unknown_image_encoded, path_un, face_locations, unknown_image):
	face_names = []
	for x, face_encoding in enumerate(unknown_image_encoded):

		match = face_recognition.compare_faces(char_known_faces, face_encoding)
		name = "Unknown"

		# for index, value in enumerate(match):
		if True in match:
			face_names.append(list(compress(char_names, match)))
	# print(path_un, "char_names: ", face_names)
	# print(path_un, " match: ", match, " face_names: ", face_names)
				# print(path_un, "char_names: ", char_names)
	# print(path_un, "char_names: ", face_names)
	# char_unknown_faces.append(unknown_image)
	# print(path_un)
	draw_faces(face_names, face_locations, unknown_image, path_un)

def new_dir(image, path_un):
	# os.chdir(newdir)
	if not path_initial:
		# print("my path: ", path_un.split("unknown_images/", 1)[1])
		# print("pathNew", pathNew)
		# os.chdir(pathNew)
		face_image = image
		pil_image = Image.fromarray(face_image)
		pil_image.save(path_un)
		# cv2.imwrite(path_un.split("unknown_images/", 1)[1], pil_image)
		# cwd



def draw_faces(face_names, face_loc, image, path_un):
	# print("")
	for (top, right, bottom, left), name in zip(face_loc, face_names):

	    # # Draw a box around the face
	    # cv2.rectangle(image, (left+10, top+10), (right+10, bottom+10), (0, 0, 255), 2)

	    # # Draw a label with a name below the face
	    # cv2.rectangle(image, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
	    # font = cv2.FONT_HERSHEY_DUPLEX
	    # cv2.putText(image, name[0], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

	    outputCheck.write(name[0] + '\n')

	new_dir(image, path_un)

 



def get_directory(rootdir):
	for subdir, dirs, files in os.walk(rootdir):
		# print("---folder name: ", subdir)
		for file in files:
			if('.DS_Store' not in file):
				# print(os.path.join(subdir, file))
				get_chars(os.path.join(subdir, file))
				char_names.append(file)


def get_unknown_directory(unknownDir):
	for file in os.listdir(unknownDir):
		if('.DS_Store' not in file):
			print(file)

			outputCheck.write(file + '\n')

			get_unknown_chars(os.path.join(unknownDir,file))

def face_recog_main(un_face):
	#known faces (i.e. characters)
	rootdir = '/Users/almas/Documents/Research/face_recog/char_faces/'
	assert os.path.isdir(rootdir)

	# pictures to evaluate
	unknownDir = un_face
	print un_face
	# .../Research/face_recog/rcnn_recog_faces/ep_1x03

	outputCheck.write(un_face.split('/ep')[1] + '\n')

	cwd = os.getcwd()
	get_directory(rootdir)
	get_unknown_directory(un_face)



