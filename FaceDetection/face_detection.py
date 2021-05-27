import cv2
import dlib

# Takes URL of an image and returns an array of face coordinates for all 
# detected faces in that image

def get_face_rects(url):
	# Load the detector
	detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
	
	# read the image
	img = cv2.imread(url)
	
	# Convert image into grayscale
	gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
	
	# Stores the coordinates of the detected faces
	face_coordinates = []
	
	# Rectangles that contain faces
	rects = detector(gray, 1)
	
	# Iterate over face rectangles
	for (i, rect) in enumerate(rects):
	    x1 = rect.rect.left()
	    y1 = rect.rect.top()
	    x2 = rect.rect.right()
	    y2 = rect.rect.bottom()
	    # Adds upper-left and lower-right corner to the face_coordinates array
	    face_coordinates.append(((x1, y1), (x2, y2)))

	return face_coordinates
