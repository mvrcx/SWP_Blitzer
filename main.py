import os
import FaceDetection.face_detection as fd
from typing import List, Dict


"""
This script allows the user to classify images into 3 categories, based on the visibility of faces inside
them. The categories are labeled as red, yellow and green. During execution the corresponding folders for 
each category are created inside the clean_data directory (constant). 
Images without faces are categorised as red, those with partially visible faces categorised as yellow and 
fully visible faces are categorised as green. 

To execute, make sure the input and output directories are located at the same path as this main.py file, 
as well as the FaceDetection directory. 

To controll the threshold for the partially covered faces, change the yellow_folder_threshold in the 
Constants. A higher threshold corresponds to more images being classified as yellow. 

To see more documentation about the project visit: https://github.com/mvrcx/SWP_Blitzer
"""


# -------------------------------------------------------------------------------------------------------- #

# Constants


raw_data = "input_files"							# input directory
clean_data = "output_files"							# output directory with red, green, yellow folders

accepted_image_formats = ["jpg", "png", "jpeg"]		# accepted image formats

yellow_folder_threshold = 0.2                       # threshold to determine covered faces (the higher, 
                                                    # the more images are classified as yellow)

# -------------------------------------------------------------------------------------------------------- #

def get_image_urls(path: str) -> List[str]:
    """Returns URL's of all images in the data_raw folder
    
    Parameters
    ----------
    path : str
        The location, were the images are located
        
    Returns
    -------
    filenames : List[str]
    """

    print("Looking for images in "+raw_data)
    filenames = []
    
    # Move to the raw_data directory, to access the images
    os.chdir(path)
    
    # loop over every file in the current directory (raw_data)
    for root, directories, files in os.walk("."):
    	for i, filename in enumerate(files): 
    		print("\r"+"Collecting filenames... "+str(i+1)+"/"+str(len(files)), end="")
    		
    		# check if file has accepted format
    		if any(image_format in filename for image_format in accepted_image_formats):
    			filenames.append(raw_data+"/"+filename)

    # change back to original directory
    os.chdir("..")
    return filenames

# -------------------------------------------------------------------------------------------------------- #

def classify_images() -> Dict[str, int]:
    """Returns a dictionary that stores the classification for each URL from get_image_urls
        0 (red): no faces detected in image
        1 (yellow): face detected, but covered
        2 (green): face detected and person identifiable
    
    Parameters
    ----------
    None
      
    Returns
    -------
    classifications : Dict[str, int]
        Dictionary containing a classification (0, 1, or 2) for each filename as the key
    """

	classifications = {}
	filenames = get_image_urls(raw_data)
	print("\nBeginning image classification.")
	
	# iterate through all files from raw_data and analyse for faces 
	for i, filename in enumerate(filenames):
		print("\r"+"Classifiing images... "+str(i+1)+"/"+str(len(filenames)), end="")
		os.chdir("FaceDetection")
		faces = fd.get_face_rects("../"+filename)
		
		# Classifiing the image 
		if len(faces) == 0:
			classifications[filename] = 0     
		else: 
		    for face in faces: 
		        if face[2] < yellow_folder_threshold:
		            classifications[filename] = 1
		            break
		        else: 
		            classifications[filename] = 2     

		os.chdir("..")
	print("\nImage classification completed.")
	return classifications

# -------------------------------------------------------------------------------------------------------- #

def create_folder(path: str) -> None:
    """Creates a folder at a path, if it doesn't already exist
    
    Parameters
    ----------
    path : str
        The folder path, that should be created
        
    Returns
    -------
    None
    """

	if not os.path.exists(path):
		os.makedirs(path)
	return

# -------------------------------------------------------------------------------------------------------- #

def move_to_folders(classifications: Dict[str, int]) -> None:
    """Moves the images from raw_data to their specific folder in data_clean (red, yellow, or green)
    
    Parameters
    ----------
    classifications : Dict[str, int]
        Dictionary containing a classification (0, 1, or 2) for each filename as the key 
        
    Returns
    -------
    None
    """

	create_folder(clean_data+"/red")
	create_folder(clean_data+"/yellow")
	create_folder(clean_data+"/green")
	
	# iterates through all classifications and moves the classified images to the corresponding directories
	for classification in classifications:
		if classifications[classification] == 0:
			os.replace(classification, clean_data+"/red/"+classification[len(raw_data):])
		elif classifications[classification] == 1:
			os.replace(classification, clean_data+"/yellow/"+classification[len(raw_data):])
		else:
			os.replace(classification, clean_data+"/green/"+classification[len(raw_data):])

# -------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
	move_to_folders(classify_images())

# -------------------------------------------------------------------------------------------------------- #