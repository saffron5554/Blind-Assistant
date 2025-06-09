import cv2
import time
import pyttsx3
from ultralytics import YOLO

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load YOLOv8 model (switch to yolov8s.pt for better accuracy)
model = YOLO("yolov8s.pt")

# Allowed object classes to announce
allowed_classes = {"person", "chair", "bottle", "cup", "dog"}

# Start webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

# Spoken tracking and timer
spoken_objects = set()
last_spoken_time = time.time()
reset_interval = 5  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Optional: Improve contrast (good in low light)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    frame = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    # Run detection
    results = model(frame, verbose=False)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Reset spoken objects every few seconds
    if time.time() - last_spoken_time > reset_interval:
        spoken_objects.clear()
        last_spoken_time = time.time()

    # Track objects in current frame
    current_objects = set()

    # Confidence threshold
    for box in results[0].boxes:
        if box.conf[0] < 0.5:
            continue  # Skip low-confidence detection

        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]

        # Only announce selected object types
        if class_name in allowed_classes:
            current_objects.add(class_name)

    # Announce new objects
    new_objects = current_objects - spoken_objects
    for obj in new_objects:
        message = f"{obj} ahead"
        print(f"Speaking: {message}")
        engine.say(message)
        engine.runAndWait()

    # Update spoken list
    spoken_objects.update(new_objects)

    # Show annotated frame
    cv2.imshow("Blind Assistant - YOLOv8 Enhanced", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
