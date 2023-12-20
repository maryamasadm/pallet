from PIL import Image
import cv2
import numpy as np
import os
from ultralytics import YOLO
import time
import torch
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated


def ms_to_fps(milliseconds):
    return 1000 / milliseconds


def process_image(model_path, image_path):
    if torch.backends.mps.is_available():
        mps_device = torch.device("mps")
        x = torch.ones(1, device=mps_device)
        print(x)
    else:
        print("MPS device not found.")

    device = torch.device("mps")

    model = YOLO(model_path)
    model.to(device)
    print('torch.cuda.device_count() = ', torch.cuda.device_count())

    # Check if the path is a directory or a single image
    if os.path.isdir(image_path):
        folder_path = image_path
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    elif os.path.isfile(image_path):
        folder_path = os.path.dirname(image_path)
        image_files = [os.path.basename(image_path)]
    else:
        print("Invalid path.")
        return

    # going through the image folder and run the yolo for them
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        results = model.predict(source=image_path, imgsz=640, conf=0.9,  save=True)

    # compute the FPS inference
    inference_time_ms = results[0].speed['inference']  # taken from your YOLO result
    fps = ms_to_fps(inference_time_ms)
    print(f"Inference FPS: {fps:.2f}")
    
    # If a single image is processed, display the result
    if len(image_files) == 1:
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            img = cv2.cvtColor(im_array[..., ::-1], cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            # Load the original image
            original_img = cv2.imread(image_path)
            # Resize the original image to match the dimensions of the predicted image
            original_img = cv2.resize(original_img, (im_array.shape[1], im_array.shape[0]))

            # Concatenate the original and predicted images horizontally
            concatenated_img = np.hstack((original_img, im_array))

            # Display the concatenated image using OpenCV
            cv2.imshow('Original vs Predicted', concatenated_img)
            cv2.waitKey(0)  # Wait for a key press to close the image window
            cv2.destroyAllWindows()  # Close all OpenCV windows