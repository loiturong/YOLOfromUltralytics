# Object Detecion with YOLO
This project build a YOLO system that can detect fruit that is durian, apples, dragon fruits, banana, and oranges

## Overview
YOLO is a Deeplearning Architecture that can detect object using IoU post-process. However, later YOLO like YOLOv10, this post-processing mechanism is cut.
This project uses pre-trained weight from YOLO8n and finetune for fruit detection task.

## DATA
Dataset is collected by download random fruit online.

## Train Model
in [notebook](./Yolo_train.ipynb)

## result
precision: 64.6 \         recall: 42.76

mAP50: 44.06     \       mAP50-95: 18.48

fitness: 21.04

## Using

install requirements `pip install -r requirements.txt`

you can further train this model in [notebook](./Yolo_train.ipynb)

you can also run the [main script](./main.py) for UI inference section.
