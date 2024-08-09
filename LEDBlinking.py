import RPi.GPIO as GPIO
from time import sleep
delay=0.1
InPin=40
OutPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(InPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(OutPin, GPIO.OUT)
try:
    while True:
        readVal=GPIO.input(InPin)
        if readVal==1:
            GPIO.output(OutPin, 0)
        else:
            GPIO.output(OutPin, 1)
except KeyboardInterrupt:
    GPIO.cleanup()
