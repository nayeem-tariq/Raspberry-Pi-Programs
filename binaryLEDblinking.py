import RPi.GPIO as GPIO
from time import sleeo 

led_pins = [29,31,33,35,37]

GPIO.setmode(GPIO.BOARD)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def display_number(number):
    binary_representation = f"{number:05b}" 
    for i in range(5):
        GPIO.output(led_pins[i], int(binary_representation[4 - i]))

try:
    for count in range(32):
        display_number(count)
        sleep(1)
finally:
    GPIO.cleanup()

