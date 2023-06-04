import RPi.GPIO as GPIO
from time import sleep
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,1)
except KeyboardInterrupt:
    GPIO.cleanup()

