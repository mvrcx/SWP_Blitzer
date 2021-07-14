import cv2
import dlib
from typing import List, Tuple


"""
This script allows the user to detect faces within a given image, by returning a list of tuples for each 
face, containing the upper-left and lower-right corner of the rectangle around the face and the confidence
for the prediction. 

For the face-detection the algorithm uses dlib's CNN Face Detector. 
More information can be found here: http://dlib.net/cnn_face_detector.py.html .
"""


# -------------------------------------------------------------------------------------------------------- #

def get_face_rects(url: str) -> List[Tuple[Tuple[int, int], Tuple[int, int], float]]:
    """Gets an image and returns the face-coordinates + the confidence in the prediction
    
    Parameters
    ----------
    url : str
        The path of the given image
    
    Returns
    -------
    face_coordinates : List[Tuple[Tuple[int, int], Tuple[int, int], float]]
        A list of tuples of the coordinates for each face + the confidence in the prediction of the face 
    """

	# Load the detector
	detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
	
	# read the image
	img = cv2.imread(url)
	img = img[0:int(img.shape[0]/2)]
	
	# Convert image into grayscale
	gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
	
	# Stores the coordinates of the detected faces
	face_coordinates = []

    # Detecting faces in gray image
	faces = detector(gray, 1)

	# Iterate over face rectangles
	for i, face in enumerate(faces):
	    x1 = face.rect.left()
	    y1 = face.rect.top()
	    x2 = face.rect.right()
	    y2 = face.rect.bottom()
	    # Adds upper-left and lower-right corner to the face_coordinates array
	    face_coordinates.append(((x1, y1), (x2, y2), face.confidence))
	    
	return face_coordinates

# -------------------------------------------------------------------------------------------------------- #
