import paho.mqtt.client as mqtt
import time
import random
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
log_path = os.path.join(base, "logs", "pub_humidity.log")
log_file = open(log_path, "a")

STUDENT_ID = 12220600

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def publish_humidity():
    hum = round(random.uniform(40, 70), 2)
    message = f'{{"Humidity": {hum}, "ID": {STUDENT_ID}}}'
    client.publish("lab/humidity", message)
    log_file.write(message + "\n")
    print("Humidity Published:", message)

while True:
    publish_humidity()
    time.sleep(2)

log_file.close()