import adafruit_dht
import time
from board import *

DHT_PIN = 4
DHT_SENSOR = adafruit_dht.DHT11(DHT_PIN)

temperature = DHT_SENSOR.temperature
humidity = DHT_SENSOR.humidity

for x in range(6):
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);


DHT_SENSOR.exit()