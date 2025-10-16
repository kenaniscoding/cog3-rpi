import cv2
import RPi.GPIO as GPIO
import time
import os

# === GPIO Setup ===
BUTTON_PIN = 23  # Choose your digital input pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# === Create/Find Next Frame Number ===
def get_next_frame_number(directory='.', prefix='frame_', extension='.jpg'):
    existing = [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith(extension)]
    numbers = []
    for f in existing:
        try:
            number = int(f[len(prefix):-len(extension)])
            numbers.append(number)
        except ValueError:
            continue
    return max(numbers, default=0) + 1

# === Camera Setup ===
cap = cv2.VideoCapture(0)  # Use the default camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press the button to capture an image. Press Ctrl+C to exit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Show the camera feed (optional)
        cv2.imshow("Live Feed", frame)

        # Check button press
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            frame_num = get_next_frame_number()
            filename = f"frame_{frame_num}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            time.sleep(0.5)  # Debounce delay to avoid multiple captures

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
