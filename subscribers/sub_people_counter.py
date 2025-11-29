import paho.mqtt.client as mqtt
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
log_path = os.path.join(base, "logs", "sub_people_counter.log")
log_file = open(log_path, "a")

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")
    log_file.write(f"{msg.payload.decode()}\n")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.subscribe("lab/people_counter")
client.loop_forever()
log_file.close()
