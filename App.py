from flask import Flask, Response, render_template
import cv2
from ultralytics import YOLO
import pyttsx3 
import threading
import time

app = Flask(__name__)

# Load the YOLOv8 model
model = YOLO("yolov8s.pt")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed of speech

# Open the webcam
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Object categories to detect
TARGET_CLASSES = {"person", "car", "bicycle", "pole", "staircase"}

# Flag to prevent continuous speech interruptions
last_command_time = 0
command_delay = 2  # seconds

def speak(text):
    """Function to convert text to speech in a separate thread."""
    global last_command_time
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()

def analyze_frame(results):
    """Analyze frame and continuously provide voice guidance based on detected objects."""
    detected_objects = set()

    for result in results:
        for box in result.boxes:
            cls = result.names[int(box.cls[0])]
            if cls in TARGET_CLASSES:
                detected_objects.add(cls)

    if detected_objects:
        speak("Detected: " + ", ".join(detected_objects))

    if "staircase" in detected_objects:
        speak("Caution! Staircase ahead. Watch your step.")

def generate_frames():
    while True:
        success, frame = webcam.read()
        if not success:
            break

        results = model(frame)
        frame = results[0].plot()  # Draw detections

        analyze_frame(results)  # Analyze detected objects

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
