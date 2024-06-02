import cv2
import numpy as np
import torch
from torchvision.models.detection import  ssdlite320_mobilenet_v3_large
from torchvision.transforms import functional as F
from coco_names import COCO_CLASS_NAMES






# Load SSD with MobileNetV3 model
def load_ssd_mobilenet_model():
    return ssdlite320_mobilenet_v3_large(pretrained=True).eval()

# Function to perform object detection and draw bounding boxes
def detect_and_draw(model, frame):
    # Convert frame to tensor
    tensor_frame = F.to_tensor(frame).unsqueeze(0)

    # Perform object detection
    with torch.no_grad():
        predictions = model(tensor_frame)

    # Process detection results
    for prediction in predictions:
        for box, label, score in zip(prediction['boxes'], prediction['labels'], prediction['scores']):
            if score >= 0.5:  # Confidence threshold
                label_idx = label.item() - 1
                if 0 <= label_idx < len(COCO_CLASS_NAMES):
                    label_text = f"{COCO_CLASS_NAMES[label_idx]}: {score:.2f}"
                    box = box.int().tolist()
                    frame = cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                    frame = cv2.putText(frame, label_text, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    print(f"Warning: Label index {label_idx} out of range")
    return frame

# Choose model (Mask R-CNN or SSD with MobileNetV3)
model = load_ssd_mobilenet_model()  # Change to load_ssd_mobilenet_model() for SSD

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Perform object detection and draw bounding boxes
    frame = detect_and_draw(model, frame)

    # Display the frame
    cv2.imshow("Object Detection", frame)
   

    # Break the loop when 'e' is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
