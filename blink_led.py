# 4. Open the Thonny Python IDE and create a new Python script named "blink_led.py" saved at the Documents folder. Enter the following simple code to blink the LED. Run the script and take a video of the setup to show that it is working.

import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
