import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
delay=0.1
InPin=40
OutPin=38
GPIO.setup(OutPin, GPIO.OUT)
GPIO.setup(InPin, GPIO.IN)
try:
    while True:
        readVal=GPIO.input(InPin)
        if readVal==1:
            GPIO.output(OutPin, 0)
        else:
            GPIO.output(OutPin, 1)
except KeyboardInterrupt:
    GPIO.cleanup()
