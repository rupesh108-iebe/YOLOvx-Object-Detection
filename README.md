# YOLOvx Vehicle & License Plate Detection

This project contains object detection models and datasets developed over a one-month internship. The system leverages YOLO object detection models to identify and locate vehicles and license plates from images.

## Project Structure

```text
yolovx/
├── datasets/                 # Unzipped datasets for YOLO 
│   ├── License_Plates_YOLOv5/
│   ├── Yolo08_v1_YOLOv8/
│   └── Yolo08_v2_YOLOv8/
├── models/                   # Best trained model weights (.pt files)
├── notebooks/                # Google Colab notebooks containing training scripts
├── .gitignore                # Git configuration
└── README.md                 # Project Documentation
```

## Datasets
The datasets were curated and downloaded through Roboflow and contain annotations split into `train`, `valid`, and `test` batches.
*   **YOLOv5 Dataset**: Annotated for `license-plate` and `vehicle`.
*   **YOLOv8 Dataset**: Annotated for `Plate`, `front`, and `rear` of vehicles. Versioned for iterative improvements.

**📥 Download the Datasets here:** [Google Drive Link](https://drive.google.com/drive/folders/11bkQ--AqfTcqEJty_-ZBQ11SwjC6b3VD?usp=sharing)

## Models
The model files are the results of training passes on Colab using the `ultralytics` framework. The learned parameters are preserved in the `best.pt` tracking files. 
These files are included directly in the `models/` array of this repository so that you can pull this code and instantly run inference or testing without needing to train from scratch.

## Code Integration
Training scripts have been authored primarily utilizing **Google Colab** environments. If you want to replicate the results:
1. Copy the `.ipynb` files from Colab to the `notebooks/` directory.
2. Ensure you have dependencies installed (e.g., `pip install ultralytics`).
3. Point your training run paths to the downloaded `datasets/` folders here.

## Contact / Maintainer
Rupesh Nandale
