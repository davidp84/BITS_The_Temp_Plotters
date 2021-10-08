import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

pwmOut = GPIO.PWM(8, 200)

pwmOut.start(0)

dutyCycle = 1

# Main program loop

# while(1):
# 
#    time.sleep(0.2)
#    dutyCycle = dutyCycle + 1
#    if(dutyCycle > 100):
#        dutyCycle = 0
#    pwmOut.ChangeDutyCycle(100 - dutyCycle)

for x in range(5):
    pwmOut.ChangeDutyCycle(100)
    time.sleep(5)
    pwmOut.ChangeDutyCycle(0)
    time.sleep(5)
    
    
    