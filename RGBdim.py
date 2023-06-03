import RPi.GPIO as GPIO
from time import sleep
import sys
GPIO.setmode(GPIO.BOARD)

rPin=40
rPin_out=33
rcounter=0.99
rOld=1
GPIO.setup(rPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rPin_out,GPIO.OUT)
rPWM=GPIO.PWM(rPin_out,100)
rPWM.start(int(rcounter))

gPin=38
gPin_out=36
gcounter=0.99
gOld=1
GPIO.setup(gPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gPin_out,GPIO.OUT)
gPWM=GPIO.PWM(gPin_out,100)
gPWM.start(int(gcounter))

bPin=31
bPin_out=37
bcounter=0.99
bOld=1
GPIO.setup(bPin,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(bPin_out,GPIO.OUT)
bPWM=GPIO.PWM(bPin_out,100)
bPWM.start(int(bcounter))
try:
    while True:
        redRead=GPIO.input(rPin)
        greenRead=GPIO.input(gPin)
        blueRead=GPIO.input(bPin)
        if redRead==1 and rOld==0:
            print(f"I am reading red {rcounter}")
            rcounter =rcounter*1.58
            if rcounter>98:
                rcounter=0.99
            rPWM.ChangeDutyCycle(int(rcounter))
        if greenRead==1 and gOld==0:
            print(f"I am reading green {gcounter}")
            gcounter =gcounter*1.58
            if gcounter>98:
                gcounter=0.99
            gPWM.ChangeDutyCycle(int(gcounter))
        if blueRead==1 and bOld==0:
            print(f"I am reading blue {bcounter}")
            bcounter =bcounter*1.58
            if bcounter>98:
                bcounter=0.99
            bPWM.ChangeDutyCycle(int(bcounter))
        rOld=redRead
        gOld=greenRead
        bOld=blueRead
        sleep (0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()    
