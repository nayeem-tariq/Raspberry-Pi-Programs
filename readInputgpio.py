import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
InPin=40
GPIO.setup(InPin, GPIO.IN)
try:
    while True:
        readVal=GPIO.input(InPin)
        print(readVal)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
