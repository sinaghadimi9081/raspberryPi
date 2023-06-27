#just checking
import RPi.GPIO as GPIO
from time import sleep
import ADC0834

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        analogVal=ADC0834.getResult(0)
        print(analogVal)
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()