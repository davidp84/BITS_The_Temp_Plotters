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

GPIO.setup(14, GPIO.OUT)

pwmOut = GPIO.PWM(14, 200)

pwmOut.start(0)

# this try/except is just to give a nicer error message for the Runtime error I get sometimes
try:

    print("start of script")

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
            print("-- values written to file --")
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
                if temperature >= 50:
                    print("Temperature above threshold!")
                    pwmOut.ChangeDutyCycle(100)
                    subprocess.run(['echo "Test - high temp alert" | msmtp tempplotters@gmail.com'],shell=True)
                if temperature < 50:
                    print("Temperature normal")
                    print("fan test, spin up")
                    pwmOut.ChangeDutyCycle(100)
                    subprocess.run(['echo "Test - no alert, all is well" | msmtp tempplotters@gmail.com'],shell=True)
                    time.sleep(2)
                    print("fan test, spin down")
                    pwmOut.ChangeDutyCycle(0)
                    time.sleep(2)
                if humidity >= 60:
                    print("Humidity above threshold!")
                    subprocess.run(['echo "Test - high humidity alert" | msmtp tempplotters@gmail.com'],shell=True)
        else:
            print("Sensor failure. Check wiring.")

except RuntimeError:
    print("Damn, the script crashed")

finally:
    print("end of script")

DHT_SENSOR.exit()
GPIO.cleanup()