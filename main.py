import os
import FaceDetection.face_detection as fd
from FaceDetection.face_detection import Net
import FaceDetection.landmark_detection as ld



# Constants

raw_data = "raw_data"								# directory with images that need to be classified
clean_data = "clean_data"							# directory that contains the classifications
accepted_image_formats = ["jpg", "png", "jpeg"]		# file formats that are accepted and loaded as images


# Returns URL's of all images in the data_raw folder

def get_image_urls():
	filenames = []
	
	# Move to the raw_data directory, to access the images
	os.chdir(raw_data)
	
	# loop over every file in the current directory (raw_data)
	for root, directories, files in os.walk("."):
		for filename in files: 
			
			# check if file has accepted format
			if any(image_format in filename for image_format in accepted_image_formats):
				filenames.append(raw_data+"/"+filename)

	# change back to original directory
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
	
	# iterate through all files from raw_data and analyse for faces 
	for filename in filenames:
		print("\r"+str(int(filenames.index(filename)/len(filenames)*100))+"%", end="")
		os.chdir("FaceDetection")
		faces = fd.get_face_rects("../"+filename)
		landmark_grayscales = ld.get_gray_scale_of_landmarks_for("../"+filename, faces)
		print(fd.is_covered(landmark_grayscales[0]))
		# Classifiing the image 
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
	
	# iterates through all classifications and moves the classified images to the corresponding directories
	for classification in classifications:
		if classifications[classification] == 0:
			os.replace(classification, clean_data+"/red/"+classification[9:])
		else:
			os.replace(classification, clean_data+"/green/"+classification[9:])



if __name__ == "__main__":
	move_to_folders(classify_images())

