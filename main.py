import paho.mqtt.client as mqtt
import time
from gpiozero import DistanceSensor
from gpiozero import LED

broker_address = "10.202.18.117"
broker_port = 1883
client = mqtt.Client()

client.connect(broker_address, broker_port)
client.loop_start()

topic = "sensor"
topic_demo = "apagar"
trigger_ = 25
echo_ = 23

R = LED(4)

sensor = DistanceSensor(echo=echo_, trigger=trigger_, max_distance=4)


def on_message(client, userdata, message):
    data = message.payload.decode()
    print("---",data)
    if(data == "1"):
         R.on()
    elif(data == "0"):
        R.off()
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
    
client.on_message = on_message

while True:
    distance = sensor.distance
    print(distance)
    time.sleep(0.5)
    client.publish(topic, distance)
    client.subscribe(topic_demo)
    
    if distance <= 0.5:
        print("Persona cerca")

client.loop_forever()

