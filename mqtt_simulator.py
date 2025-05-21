import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

while True:
    value = random.uniform(70, 80)
    client.publish("sfaaas/factory1/temperature", value)
    print(f"Sent: {value}")
    time.sleep(2)