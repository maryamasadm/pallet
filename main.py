from functions.process_image import process_image

import sys
import os
PYTORCH_ENABLE_MPS_FALLBACK=1

def main(model_path, image_path):
    process_image(model_path, image_path)
    

if __name__ == "__main__":

    model_path = 'weights/yolov8_640.pt'
    
    # Check if the user provided an image path as a command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    # Get the image path from the command-line argument
    image_path = sys.argv[1]
    '''
    # Check if the entered path is valid
    if not os.path.isfile(image_path):
        print("Invalid path. Please make sure the file exists.")
        sys.exit(1)
        '''
 # Call the function to process the image
    main(model_path, image_path)