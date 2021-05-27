import os
import FaceDetection.face_detection as fd


# Constants

raw_data = "raw_data"
clean_data = "clean_data"
accepted_image_formats = ["jpg", "png", "jpeg"]

# Returns URL's of all images in the data_raw folder

def get_image_urls():
	filenames = []
	os.chdir(raw_data)
	for root, directories, files in os.walk("."):
		for filename in files: 
			if any(image_format in filename for image_format in accepted_image_formats):
				filenames.append(raw_data+"/"+filename)
	os.chdir("..")
	return filenames

# Returns a dictionary that stores the classification 
# for each URL from get_image_urls
# 0 (red): no faces detected in image
# 1 (yellow): face detected, but covered
# 2 (green): face detected and person identifiable

def classify_images():
	classifications = {}
	filenames = get_image_urls()
	print("Looking for faces...")
	for filename in filenames:
		print("\r"+str(int(filenames.index(filename)/len(filenames)*100))+"%", end="")
		os.chdir("FaceDetection")
		faces = fd.get_face_rects("../"+filename)
		if len(faces) == 0:
			classifications[filename] = 0     
		else: 
			classifications[filename] = 2     
		os.chdir("..")
	print("\r"+str(100)+"%")
	return classifications

# Creates a folder at a path, if it doesn't already exist

def create_folder(path):
	if not os.path.exists(path):
		os.makedirs(path)
	return

# Moves the images from raw_data to their specific folder in 
# data_clean (red, yellow, or green)

def move_to_folders(classifications):
	create_folder(clean_data+"/red")
	create_folder(clean_data+"/green")
	for classification in classifications:
		if classifications[classification] == 0:
			os.replace(classification, clean_data+"/red/"+classification[9:])
		else:
			os.replace(classification, clean_data+"/green/"+classification[9:])



move_to_folders(classify_images())