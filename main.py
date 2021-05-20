import os
import cv2
import dlib
from matplotlib import pyplot as plt



def get_face_rects(url):
	# Load the detector
	detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
	
	# read the image
	img = cv2.imread(url)
	
	# Convert image into grayscale
	gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
	
	# Use detector to find landmarks
	face_coordinates = []
	rects = detector(gray, 1)
	for (i, rect) in enumerate(rects):
	    x1 = rect.rect.left()
	    y1 = rect.rect.top()
	    x2 = rect.rect.right()
	    y2 = rect.rect.bottom()
	    # Rectangle around the face
	    face_coordinates.append(((x1, y1), (x2, y2)))
	print("Detected " + str(len(rects)) + " faces")
	return face_coordinates


	
def get_image_urls():
	filenames = []
	os.chdir("data")
	for root, directories, files in os.walk("."):
		for filename in files: 
			if "jpg" in filename or "png" in filename or "jpeg" in filename:
				filenames.append("data/"+filename)
	return filenames

def classify_images():
	classifications = {}
	filenames = get_image_urls()
	for filename in filenames:
		print(filename)
		faces = get_face_rects(filename)
		print(len(faces))
	return classifications

classify_images()
