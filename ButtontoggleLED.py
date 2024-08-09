import RPi.GPIO as GPIO
from time import sleep
delay=0.1
InPin=40
OutPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(InPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(OutPin, GPIO.OUT)

led_state=0
readValue=1
readValue_old=1

try:
    while True:
        readValue=GPIO.input(InPin)
        if readValue==1 and readValue_old==0:
            led_state=not led_state
            GPIO.output(OutPin, led_state)

        readValue_old=readValue


except KeyboardInterrupt:
    GPIO.cleanup()
