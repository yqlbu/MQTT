# MQTT Client demo
# Creator: Kevin Yu
 
import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime
from utils import on_log, on_connect, on_disconnect, on_message, get_ip

# Create an MQTT client and attach our routines to it.
broker="127.0.0.1"

client=mqtt.Client() #new instance
# Bind call back function
client.on_connect=on_connect 
client.on_disconnect=on_disconnect
client.on_message=on_message

# Enable log
#client.on_log=on_log

# Connect to broker
print("Connecting to broker {}".format(broker))
client.connect(broker,1883,60)

# Publish a message
# It is set to send the message every 5 seconds by default
while True:
    # Create a msg object
    data={
        "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "client":get_ip()[0],
        "client_ip":get_ip()[1],
        "msg":"Hello"
    }

    # Encode message to Json String
    data_out=json.dumps(data)
    client.publish("test",data_out)
    print("Msg has been sent!")
    time.sleep(5)

client.disconnect() # Disconnect
