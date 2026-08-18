import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3
import time

# ---------------------------
# LOAD AI MODEL & LABELS
# ---------------------------
model = load_model("keras_model.h5", compile=False)

with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# ---------------------------
# TEXT TO SPEECH SETUP
# ---------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------------------
# CAMERA SETUP
# ---------------------------
def get_camera():
    for index in [0, 1, 2]:
        for backend in [cv2.CAP_DSHOW, cv2.CAP_MSMF, None]:
            if backend is not None:
                cap = cv2.VideoCapture(index, backend)
            else:
                cap = cv2.VideoCapture(index)
            
            if cap.isOpened():
                # Try to read a frame to confirm it's actually working
                ret, frame = cap.read()
                if ret:
                    print(f"Camera found at index {index}")
                    return cap
                cap.release()
    return None

cap = get_camera()

if cap is None:
    print("Error: No working camera detected. Please check your connections.")
    exit()

print("System Ready. Press 'c' to detect currency. Press 'q' to quit.")

# ---------------------------
# PREDICTION FUNCTION
# ---------------------------
def predict_note(frame):
    img = cv2.resize(frame, (224, 224))
    img = np.asarray(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    index = np.argmax(prediction)
    confidence = prediction[0][index]

    return labels[index], confidence

# ---------------------------
# MAIN LOOP
# ---------------------------
last_spoken = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Currency Detector", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):   # Press 'c' to capture
        label, confidence = predict_note(frame)

        print(f"Detected: {label} ({confidence*100:.2f}%)")

        # Avoid repeating same voice again and again
        if confidence > 0.80 and label != last_spoken:
            speak(f"{label} rupees")
            last_spoken = label
        else:
            speak("Try again")

        time.sleep(1)

    elif key == ord('q'):
        break

# ---------------------------
# CLEANUP
# ---------------------------
cap.release()
cv2.destroyAllWindows()