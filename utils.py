import paho.mqtt.client as mqtt
import json
import socket

# The callback for when the client receives a CONNACK response from the server.
def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
	# Subscribing in on_connect() - if we lose the connection and
    	# reconnect then subscriptions will be renewed.
        client.subscribe("test")
        print("Connection OK")
    else:
        print("Bad connection returned code=",rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))
 
def on_message(client, userdata, message):
    print("Data received!")
    # Decode message from Json to Python Dictionary
    content=json.loads(message.payload.decode("utf-8","ignore"))
    msg=content['msg']
    data={
	"topic":message.topic,	
	"content":content,
	"qos":message.qos,
	"retain_flag":message.retain
    }
    print(data)
    if msg == u'Hello': #Unicode String
        print("Received a special msg {}!".format(content['msg']))
	    # Do something

def get_ip():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    return (hostname, IPAddr)