import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
x=int(input("Enter how many times you want to blink LED: "))
for i in range(x):
    GPIO.output(11, True)
    sleep(1)
    GPIO.output(11, False)
    sleep(1)
GPIO.cleanup()
