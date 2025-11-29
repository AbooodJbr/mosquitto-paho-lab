import paho.mqtt.client as mqtt
import time
import random
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
log_path = os.path.join(base, "logs", "pub_temperature.log")
log_file = open(log_path, "a")

STUDENT_ID = 12220600

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def publish_temperature():
    temp = round(random.uniform(20, 30), 2)
    message = f'{{"tempereature": {temp}, "ID": {STUDENT_ID}}}'
    client.publish("lab/temperature", message)
    log_file.write(message + "\n")
    print("Temperature Published:", message)


while True:
    publish_temperature()
    time.sleep(2)

log_file.close()