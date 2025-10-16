# 8. Connect the four (4) LEDs and a push button to the GPIO header properly. Then, create a new Python script named "led_pattern.py" saved at the Documents folder. When the program is executed, the 4 LEDs should show a simple moving light pattern across the LEDs, with one LED lit at a time. Pressing the push button should toggle the direction of movement. Provide the code below and take a video showing that is works. Put the shared video link in your final report.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pins = [4, 18, 27, 22]
button_pin = 23

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# --- Variables ---
direction = 1  # 1 = forward, -1 = backward
index = 0      # Current LED index
delay = 0.2    # Speed of movement (seconds)
last_button_state = GPIO.LOW

# print("LED pattern program started. Press Ctrl+C to stop.")

try:
    while True:
        # --- Button check ---
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.HIGH and last_button_state == GPIO.LOW:
            direction *= -1  # Toggle direction
            print("Direction changed!")
            time.sleep(0.3)  # Debounce delay

        last_button_state = button_state

        # --- LED pattern movement ---
        # Turn off all LEDs
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)

        # Turn on current LED
        GPIO.output(led_pins[index], GPIO.HIGH)

        # Move index in current direction
        index += direction

        # Wrap around when reaching the end
        if index >= len(led_pins):
            index = 0
        elif index < 0:
            index = len(led_pins) - 1

        time.sleep(delay)

except KeyboardInterrupt:
    print("\nstopped")

finally:
    GPIO.cleanup()
    print("gpio clean")
