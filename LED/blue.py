import RPi.GPIO as GPIO
from time import sleep
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(38,GPIO.OUT)
    GPIO.output(38,1)
except KeyboardInterrupt:
    GPIO.cleanup()