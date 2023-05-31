import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
mypwm = GPIO.PWM(21,100)
try:
    while True:
        mypwm.start(50)
except KeyboardInterrupt:
    GPIO.cleanup()
