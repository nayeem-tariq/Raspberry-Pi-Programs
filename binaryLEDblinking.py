import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the LEDs
led_pins = [29,31,33,35,37]

# Setup GPIO mode
GPIO.setmode(GPIO.BOARD)

# Setup the LED pins as output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def display_number(number):
    # Convert number to binary and display on LEDs
    binary_representation = f"{number:05b}"  # 5-bit binary representation
    for i in range(5):
        GPIO.output(led_pins[i], int(binary_representation[4 - i]))

try:
    for count in range(32):
        display_number(count)
        time.sleep(1)  # Wait for 1 second before counting up
finally:
    # Cleanup GPIO settings before exiting
    GPIO.cleanup()

