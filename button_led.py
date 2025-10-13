# 6. In the Thonny Python IDE, create a new Python script named "button_led.py" saved at the Documents folder. Enter the following code to read the button's state and control the LED. Run the script and take a video of the setup to show that it is working.

import RPi.GPIO as GPIO
import time

led_pin = 17
button_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

try:
while True:
    button_state = GPIO.input(button_pin)
    if button_state == GPIO.LOW:
    GPIO.output(led_pin, GPIO.HIGH)
    else:
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.02)
except KeyboardInterrupt:
    GPIO.cleanup()
