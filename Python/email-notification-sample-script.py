import adafruit_dht
from board import *
import time
import datetime
from datetime import date
import subprocess

DHT_PIN = 4
DHT_SENSOR = adafruit_dht.DHT11(DHT_PIN)

temperature = DHT_SENSOR.temperature
humidity = DHT_SENSOR.humidity
today = date.today()
now = datetime.datetime.now().time()

print("Screen output:")

# this will output to the values to screen running 4 times at 2 second interval
# if temperature is above 23*C it'll send an email
for x in range(4):
    if humidity is not None and temperature is not None:
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        today = date.today()
        now = datetime.datetime.now().time()
        print("Temperature: {0:0.1f}C humidity={1:0.1f}%".format(temperature, humidity),"on",today,"at",now.strftime('%H:%M:%S'))
        if temperature >= 23:
            print("Temperature above threshold!")
# replace the email in the line below with the email address you want to send it to
            result = subprocess.run(['echo "This is a test" | msmtp tempplotters@gmail.com'],shell=True)
            result
        else:
            print("Temperature normal")
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(2);

DHT_SENSOR.exit()