import os
import FaceDetection.face_detection as fd

	
def get_image_urls():
	filenames = []
	os.chdir("data")
	for root, directories, files in os.walk("."):
		for filename in files: 
			if "jpg" in filename or "png" in filename or "jpeg" in filename:
				filenames.append("data/"+filename)
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
	print("\r"+str(int(filenames.index(filename)/len(filenames)*100))+"%")
	return classifications

print(classify_images())

