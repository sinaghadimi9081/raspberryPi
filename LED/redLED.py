import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
try:
	while True:
   	 	GPIO.output(40,1)
except KeyboardInterrupt:
    GPIO.cleanup()

