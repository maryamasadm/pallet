# Pallet Detection

This repository develop a prototype model for real-time detection of wooden pallets based on Yolov8.


<img src="/image.jpg" alt="wooden pallet" width="70%">
<div style="text-align:center;font-style:italic;font-size:80%">Ref</div>


## Local Installation

### Setting up the Conda Environment

To set up the Conda environment required for running the code locally on your machine, follow these steps:

```bash
    git clone https://github.com/maryamasadm/pallet.git
    cd pallet
    conda create --name pallet
    conda activate pallet
    pip install -r requirements.txt
    python main.py path/to/your/image

```
### usage

Run this and change give the folder path:

```bash
python main.py folder_path

```


**Libraries and Frameworks:**

- [YOLOv8](https://docs.ultralytics.com/): Used for object detection.


