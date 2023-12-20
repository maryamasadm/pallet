


from PIL import Image
import cv2
import numpy as np
import os
from ultralytics import YOLO
import time
import os
import torch


if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")
device = torch.device("mps")


# Load YOLO model
model = YOLO("/Users/maryam/Downloads/best.pt")
model.to(device)
print('torch.cuda.device_count() = ', torch.cuda.device_count())

# Path to the folder containing images
image_folder_path = "/Users/maryam/Desktop/Pallets.v2i.yolov8/test/images"

# List all image files in the folder
image_files = [f for f in os.listdir(image_folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Measure inference time for each image
start_time = time.time()
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(image_folder_path, image_file)

    # Perform inference on the image
    #results = model.predict(source=image_path)
    results = model.predict(source=image_path,imgsz=320, conf=0.5)
    
    #results = model(source=image_path)  # predict on an image

# Calculate total time and FPS
end_time = time.time()
total_time = end_time - start_time
total_images = len(image_files)
fps = total_images / total_time

print(f"Total time: {total_time:.2f} seconds")
print(f"Total images: {total_images}")
print(f"Frames per second (FPS): {fps:.2f}")

# Export the model
#model.export(format='onnx')