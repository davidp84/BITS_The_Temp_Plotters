from os import write
from typing import Text
import adafruit_dht
from board import *
import time
import datetime
from datetime import date
import csv
import os

DHT_PIN = 4
DHT_SENSOR = adafruit_dht.DHT11(DHT_PIN)

temperature = DHT_SENSOR.temperature
humidity = DHT_SENSOR.humidity
today = date.today()
now = datetime.datetime.now().time()

# this try/except is just to give a nicer error message for the Runtime error I get sometimes
try:

    print("Screen output:")

    # this will output to screen
    for x in range(6):
        if humidity is not None and temperature is not None:
            temperature = DHT_SENSOR.temperature
            humidity = DHT_SENSOR.humidity
            today = date.today()
            now = datetime.datetime.now().time()
            print("Temperature: {0:0.1f}C humidity={1:0.1f}%".format(temperature, humidity),"on",today,"at",now.strftime('%H:%M:%S'))
        else:
            print("Sensor failure. Check wiring.");
        time.sleep(3);

    # this will output to csv and I've put a print statement as a sanity check
    print("CSV file output")
    for x in range(6):
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        today = date.today()
        now = datetime.datetime.now().time()

        with open('sensor.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if os.stat('sensor.csv').st_size == 0:
                writer.writerow(["Temperature","Humidity","Date","Time"])
                writer.writerow([temperature,humidity,today,now.strftime('%H:%M:%S')])
            else:
                writer.writerow([temperature,humidity,today,now.strftime('%H:%M:%S')])
        time.sleep(3);

    # this will output to text and I've put a print statement as a sanity check
    print("Text file output")
    for x in range(6):
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        today = date.today()
        now = datetime.datetime.now().time()

        with open('sensor.txt', 'a') as file:
            if os.stat('sensor.txt').st_size == 0:
                headings = ['Temperature','Humidity','Date','Time']
                values = [str(temperature),str(humidity)]#,today,now.strftime('%H:%M:%S')]
                file.write("".join(headings))
                file.write("".join(values))
            else:
                values = [str(temperature),str(humidity)]#,today,now.strftime('%H:%M:%S')]
                file.write(values)
        time.sleep(3);

    file.close()

except RuntimeError:
    print("Damn, the script crashed")

DHT_SENSOR.exit()
