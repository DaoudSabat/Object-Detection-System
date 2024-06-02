import cv2
import numpy as np

# YOLO class names

from coco_names import COCO_CLASS_NAMES 

# Load YOLO model
cfg_file_path = "C:/Users/daoud/teest1/yolov3.cfg"
weights_file_path = "C:/Users/daoud/teest1/yolov3.weights"
net = cv2.dnn.readNetFromDarknet(cfg_file_path, weights_file_path)

layer_names = net.getUnconnectedOutLayersNames()

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Perform object detection
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    # Process detection results
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Draw bounding boxes on the frame
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.6)

    for i in indices:
        i = i[0] if isinstance(i, np.ndarray) else i  # Check if 'i' is an array
        box = boxes[int(i)]
        label = COCO_CLASS_NAMES[class_ids[(i)]]
        confidence = confidences[int(i)]
        color = (0, 255, 0)  # Green color for bounding box
        cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame
    cv2.imshow("Object Detection", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
