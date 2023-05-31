import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

rPin=21
GPIO.setup(rPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

gPin=20
GPIO.setup(gPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

bPin=16
GPIO.setup(bPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        redRead=GPIO.input(rPin)
        greenRead=GPIO.input(gPin)
        blueRead=GPIO.input(bPin)
        if redRead==0:
            print("I am reading red")
        if greenRead==0:
            print("I am reading green")
        if blueRead==0:
            print("I am reading blue")
except KeyboardInterrupt:
    GPIO.cleanup()
    
