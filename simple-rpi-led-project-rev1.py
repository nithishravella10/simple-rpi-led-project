# Import RPi.GPIO module - For controlling GPIO pins on RPi
import RPi.GPIO as GPIO

# Import time module - For using delays in the code
import time

# Set up the GPIO mode- Addressing GPIO pins in the view of BCM(Broadcom) 
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LEDs
green_led_pin = 17
red_led_pin = 27

# Set up the GPIO pins as OUTPUT
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the green LED
        GPIO.output(green_led_pin, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Turn off the green LED
        GPIO.output(green_led_pin, GPIO.LOW)

        # Turn on the red LED
        GPIO.output(red_led_pin, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Turn off the red LED
        GPIO.output(red_led_pin, GPIO.LOW)

except KeyboardInterrupt:
    # Clean up GPIO settings on program exit - To ensure the GPIO pins return to their default state
    GPIO.cleanup()
