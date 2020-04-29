# MQTT Client demo
# Creator: Kevin Yu
 
import paho.mqtt.client as mqtt
import time
import json
from utils import on_log, on_connect, on_disconnect, on_message, get_ip

# Create an MQTT brocker
broker=get_ip()[1]

# Create an MQTT client and attach our routines to it.
client=mqtt.Client() #new instance
# Bind call back function
client.on_connect=on_connect 
client.on_disconnect=on_disconnect
client.on_message=on_message
# Enable log
#client.on_log=on_log

# Connect to broker
print("Connecting to broker {} @ {} ".format(get_ip()[0],broker))
client.connect(broker,1883,60)
client.loop_forever()
 


