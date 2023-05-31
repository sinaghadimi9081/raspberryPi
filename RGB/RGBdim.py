import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

rPin=21
rPin_out=26
GPIO.setup(rPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rPin_out,GPIO.OUT)
rPWM=GPIO.PWM(rPin_out,100)

gPin=20
gPin_out=19
GPIO.setup(gPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gPin_out,GPIO.OUT)
gPWM=GPIO.PWM(gPin_out,100)

bPin=16
bPin_out=13
GPIO.setup(bPin,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(bPin_out,GPIO.OUT)
bPWM=GPIO.PWM(bPin_out,100)

try:
    while True:
        redRead=GPIO.input(rPin)
        greenRead=GPIO.input(gPin)
        blueRead=GPIO.input(bPin)
        if redRead==0:
            print("I am reading red")
            GPIO.output(rPin_out,1)
        if greenRead==0:
            print("I am reading green")
            GPIO.output(gPin_out,1)
        if blueRead==0:
            print("I am reading blue")
            GPIO.output(bPin_out,1)
        sleep (0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    
