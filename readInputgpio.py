import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
InPin=40
GPIO.setup(InPin, GPIO.IN)
readVal=GPIO.input(InPin)
print(readVal)
GPIO.cleanup()
