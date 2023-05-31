import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
mypwm = GPIO.PWM(40,100)
try:
    while True:
        mypwm.start(50)
except KeyboardInterrupt:
    GPIO.cleanup()
