import RPi.GPIO as GPIO 
from time import sleep
import ADC0834

GPIO.setmode(GPIO.BCM)
ADC0834.setup()
GPIO.setup(26,GPIO.OUT)
LED_PWM=GPIO.PWM(26,100)
LED_PWM.start(0)
try:
    while True:
        analogVal=ADC0834.getResult(0)
        LED_PWM.ChangeDutyCycle(int(analogVal*0.33))
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    