import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

rPin=21
rPin_out=26
rcounter=0.4
rOld=1
GPIO.setup(rPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rPin_out,GPIO.OUT)
rPWM=GPIO.PWM(rPin_out,100)

gPin=20
gPin_out=19
gcounter=0.4
gOld=1
GPIO.setup(gPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gPin_out,GPIO.OUT)
gPWM=GPIO.PWM(gPin_out,100)

bPin=16
bPin_out=13
bcounter=0.4
bOld=1
GPIO.setup(bPin,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(bPin_out,GPIO.OUT)
bPWM=GPIO.PWM(bPin_out,100)

try:
    while True:
        redRead=GPIO.input(rPin)
        greenRead=GPIO.input(gPin)
        blueRead=GPIO.input(bPin)
        rPWM.start(rcounter-0.4)
        gPWM.start(gcounter-0.4)
        bPWM.start(bcounter-0.4)
        if redRead==1 and rOld==0:
            print("I am reading red")
            rcounter *=1.58
            if rcounter>95:
                rcounter=0.99
        if greenRead==0 and gOld==0:
            print("I am reading green")
            gcounter *=1.58
            if gcounter>95:
                gcounter=0.99
        if blueRead==0 and bOld==0:
            print("I am reading blue")
            rPWM.start(bcounter)
            bcounter *=1.58
            if bcounter>95:
                bcounter=0.99
        rOld=redRead
        gOld=greenRead
        bOld=blueRead
        sleep (0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    
