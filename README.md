Project Title: Blind Assistance System using Object Detection and Voice Feedback
Description:
This project implements a real-time blind assistance system that uses a webcam and a YOLOv8 object detection model to identify important objects in the environment and provide voice feedback to the user.

The system continuously captures video frames from the webcam, detects specific objects of interest (such as person, chair, bottle, cup, dog), and announces their presence aloud using text-to-speech (TTS). This helps visually impaired users navigate their surroundings more safely.

Key Features:
Real-time Object Detection:
Utilizes the YOLOv8 (You Only Look Once) model to detect objects from the webcam feed with high speed and accuracy.

Selective Object Announcements:
Only announces specific object types that are relevant for navigation assistance (person, chair, bottle, cup, dog), avoiding information overload.

Voice Feedback:
Uses pyttsx3 for offline TTS so the system works without an internet connection. When a relevant object is detected, the system speaks e.g. "person ahead".

Smart Repetition Control:
Implements a timer to reset spoken objects every few seconds (default 5 seconds), allowing the system to announce the same object again after a short delay if it remains in view.

Contrast Enhancement:
Optionally enhances frame contrast to improve detection in low-light environments.

User Control:
Displays the annotated video feed to a window and allows the user to quit by pressing 'q'.

How it works:
Initializes the YOLOv8 object detection model (yolov8s.pt) and TTS engine.

Captures frames from the webcam.

Enhances the image contrast for better visibility in low-light.

Detects objects in the frame using YOLOv8.

For each detected object:

If the object belongs to the allowed classes, it is spoken aloud using TTS.

Previously announced objects are temporarily ignored for a short time (reset interval).

Displays the annotated frame in a window.

Runs continuously until the user presses 'q'.

Potential Use Cases:
Assisting blind or visually impaired individuals in navigating indoor and outdoor environments.

Helping users identify objects of interest in unfamiliar spaces.

Prototype for wearable visual assistance devices (smart glasses, portable systems).

Technologies Used:
YOLOv8 (ultralytics package) — deep learning-based object detection.

OpenCV (cv2) — video capture and frame processing.

pyttsx3 — offline text-to-speech synthesis.

Python 3.x — programming language.
