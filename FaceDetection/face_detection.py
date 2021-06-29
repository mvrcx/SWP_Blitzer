import cv2
import dlib

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


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
	return rects



class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(68, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        x = self.fc3(x)
        return x


def is_covered(landmark_grayscales):
    model = Net()
    model.load_state_dict(torch.load("detect_covered_face.pt", map_location=torch.device('cpu')))
    model.eval()
    
    x = np.array(landmark_grayscales)
    x = torch.from_numpy(x).float()
    prediction = model(x)
    
    if prediction.item() < 0.5:
        return False
    else: 
        return True
        


