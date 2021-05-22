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
	for filename in filenames:
		print(filename)
		os.chdir("FaceDetection")
		faces = fd.get_face_rects("../"+filename)
		os.chdir("..")
		print(len(faces))
	return classifications

classify_images()

