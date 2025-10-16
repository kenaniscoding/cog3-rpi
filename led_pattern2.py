import RPi.GPIO as GPIO
import time 

led_pins = [4, 18, 27, 22]
# led_pins =[17, 18, 27 22]
button_pin = 23

GPIO.setmode(GPIO.BCM)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

direction = 1
current_led = 0
last_button_state = GPIO.input(button_pin )

try:
    while True:
        button_state = GPIO.input(button_pin)

        if last_button_state == GPIO.HIGH and button_state == GPIO.LOW:
            direction = -direction
            time.sleep(0.2)

        last_button_state = button_state 

        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)

        GPIO.output(led_pins[current_led ], GPIO.HIGH)

        current_led += direction

        if current_led >= len(led_pins):
            current_led = 0
        elif current_led < 0:
            current_led = len(led_pins) -1

        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
