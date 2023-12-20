# Pallet Detection

This repository develop a prototype model for real-time detection of wooden pallets based on Yolov8.


<img src="/image.png" alt="wooden pallet" width="70%">



## Local Installation

### Setting up the Conda Environment

To set up the Conda environment required for running the code locally on your machine, follow these steps:

```bash
    git clone https://github.com/maryamasadm/pallet.git
    cd pallet
    conda create --name pallet
    conda activate pallet
    pip install -r requirements.txt
   
```
### usage

Run this and after you changed the folder path or image path:

```bash
python main.py folder_path_or_image_path

```


**Libraries and Frameworks:**

- [YOLOv8](https://docs.ultralytics.com/): Used for object detection.


