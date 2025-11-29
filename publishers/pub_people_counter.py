import paho.mqtt.client as mqtt
import time
import random
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
log_path = os.path.join(base, "logs", "pub_people_counter.log")
log_file = open(log_path, "a")

STUDENT_ID = 12220600

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def publish_people_count():
    people = random.randint(0, 10)
    message = f'{{"people count": {people}, "ID": {STUDENT_ID}}}'
    client.publish("lab/people_counter", message)
    log_file.write(message + "\n")
    print("People Count Published:", message)

while True:
    publish_people_count()
    time.sleep(2)

log_file.close()