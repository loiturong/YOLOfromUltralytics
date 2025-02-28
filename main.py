# This is a sample Python script.
from ultralytics import YOLO

model_file_path = "./runs/detect/train9/weights/best.pt"
# Load a model
model = YOLO(model_file_path)



if __name__ == '__main__':
    source = "./datasets/Fruit/train/images/0f7fc9fa-image_44.jpg"
    # Run batched inference on a list of images
    results = model(source, stream=True)  # return a generator of Results objects

    # Process results generator
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen

# See PyCharm help at https://www.jetbrains.com/help/pycharm/