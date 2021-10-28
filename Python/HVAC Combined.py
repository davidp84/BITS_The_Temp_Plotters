from os import write
from typing import Text
import adafruit_dht
from board import *
import time
import datetime
import RPi.GPIO as GPIO
from datetime import date
import subprocess
import csv
import os

DHT_PIN = 4
DHT_SENSOR = adafruit_dht.DHT11(DHT_PIN)
#mode = GPIO.getmode()
#print('mode is =', mode) returns 11 for the mode
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.OUT)

#pwmOut = GPIO.PWM(8, 200)

#pwmOut.start(0)

#dutyCycle = 1

def readSensor():
    
    # this try/except is just to give a nicer error message for the Runtime error I get sometimes
    try:
        print("Screen output:")
        # this will output to screen
        for x in range(6):
            temperature = DHT_SENSOR.temperature
            humidity = DHT_SENSOR.humidity
            today = date.today()
            now = datetime.datetime.now().time()
            if humidity is not None and temperature is not None:
                print("Temperature: {0:0.1f}C humidity={1:0.1f}%".format(temperature, humidity),"on",today,"at",now.strftime('%H:%M:%S'))
                values = [str(temperature),",",str(humidity),",",str(today),",",str(now.strftime('%H:%M:%S')),"\n"]
                writeData(values)
                if temperature >= 50:
                    print("Temperature above threshold!")
                    fan(100)
                    sendEmail(temp = "temp")
                if temperature < 50:
                    print("Temperature normal")
                    fan(0)
                if humidity >= 60:
                    print("Humidity above threshold!")
                    sendEmail(humid = "humid")
            else:
                print("Sensor failure. Check wiring.")
            
            time.sleep(10)          

    except RuntimeError:
        print("Damn, the script crashed")
DHT_SENSOR.exit()

readSensor()

def writeData(values):

    print("Text file output")
    with open('sensor.txt', 'a', newline='') as file:
        if os.stat('sensor.txt').st_size == 0:
            headings = ['Temperature',",",'Humidity',",",'Date',",",'Time','\n']
            value = values
            for heading in headings:
                file.write(heading)
            for value in values:
                file.write(value)
        else:
                value = values
                for value in values:
                    file.write(value)
    file.close()
    
def fan(x):
    if x == 100:
        pwmOut.ChangeDutyCycle(100)
    else:
        pwmOut.ChangeDutyCycle(0)
        
def sendEmail( fault):
    if fault == 'temp':
        subprocess.run(['echo "This is a test" | msmtp tempplotters@gmail.com'],shell=True)
    else: 
        subprocess.run(['echo "This is a test" | msmtp tempplotters@gmail.com'],shell=True)