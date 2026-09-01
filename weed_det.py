import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("C:/Users/Harsh/Documents/weed_detection_project/runs/detect/train3/weights/best.pt")

# Run detection
results = model.predict(
    source="C:/Users/Harsh/Documents/weed_detection_project/ss/img_15.jpeg",  # folder or image
    show=True,
    conf=0.25,    
    save=True
)
# Show image manually
img = results[0].plot()
cv2.imshow("Weed Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()