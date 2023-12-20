# Pallet Detection

This repository develop a prototype model for real-time detection of wooden pallets based on Yolov8.

<a href="https://lens.monash.edu/@technology/2020/06/22/1380700/mirror-ritual-ais-role-in-reframing-viewers-emotions" style="text-decoration:none">
  <img src="/image.jpg" alt="wooden pallet" width="50%">
  <div style="text-align:center;font-style:italic;font-size:80%">Ref</div>
</a>



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
**Libraries and Frameworks:**

- [YOLOv8](https://docs.ultralytics.com/): Used for object detection.


