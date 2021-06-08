import cv2
import dlib
from PIL import Image


def get_color_of_pixel(image_url, coordinate):
    im = Image.open(image_url) 
    pix = im.load()
    return pix[coordinate[0], coordinate[1]]  
    

def get_gray_scale_of_landmarks_for(image_url, faces):
    
    # Load the predictor
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    # read the image
    img = cv2.imread(image_url)
    
    # Convert image into grayscale
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
        
    gray_scales_of_landmarks = []
    for face in faces:
    
        # Create landmark object
        landmarks = predictor(image=gray, box=face.rect)
        
        landmark_grayscales_for_face = []
        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            if y < len(gray) and x < len(gray[0]):
                landmark_grayscales_for_face.append(gray[y, x])
        if len(landmark_grayscales_for_face) == 68:
            gray_scales_of_landmarks.append(landmark_grayscales_for_face)
    return gray_scales_of_landmarks