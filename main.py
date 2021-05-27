import os
import FaceDetection.face_detection as fd
import cv2

	
def get_image_urls():
	filenames = []
	os.chdir("raw_data")
	for root, directories, files in os.walk("."):
		for filename in files: 
			if "jpg" in filename or "png" in filename or "jpeg" in filename:
				filenames.append("raw_data/"+filename)
	os.chdir("..")
	return filenames

def classify_images():
	classifications = {}
	filenames = get_image_urls()
	print("Looking for faces...")
	for filename in filenames:
		print("\r"+str(int(filenames.index(filename)/len(filenames)*100))+"%", end="")
		os.chdir("FaceDetection")
		faces = fd.get_face_rects("../"+filename)
		if len(faces) == 0:
			classifications[filename] = 0     # Rot
		else: 
			classifications[filename] = 2     # Gruen
		os.chdir("..")
	print("\r"+str(100)+"%")
	return classifications
	
def create_folder(path):
	if not os.path.exists(path):
		os.makedirs(path)
	return

def move_to_folders(classifications):
	create_folder("clean_data/Rot")
	create_folder("clean_data/Gruen")
	for classification in classifications:
		if classifications[classification] == 0:
			os.replace(classification, "clean_data/Rot/"+classification[9:])
		else:
			os.replace(classification, "clean_data/Gruen/"+classification[9:])



move_to_folders(classify_images())