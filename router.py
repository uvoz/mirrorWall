# ROUTER for mirror messages
# 2019 by StrejcekBob
# tested by MakerMatty
# This module is a central router that receives mirror movements, frames and animations
#it listens to messages sent to the movemirror topic, retrieves the hub address and forwards the message to the hub
#no validation is made her to keep it light. Validation is done distributed by all hubs.
#mosquitto_pub -t movemirror -m '{"mirror":44,"ud":15.1,"lr":-25}'
import mirrormap as mm
import sys
import json
import paho.mqtt.client as mqtt
import time


#configurable variables
mqtt_broker_address ="127.0.0.1"
movemirror        ='movemirror'
playframe         ='playframe'
mqtt_broker_port    =1883

     
def routemovemirror(msg):
    j = json.loads(msg)
    address=mm.getMirrorAddress(j['mirror'])
    hub=address['hub']
    #print("routing to hub "+str(hub)+": "+json.dumps(j))
    client.publish("hub"+str(hub)+"/"+movemirror,msg)


#mosquitto_pub -t playframe -m '{"Frame": "some name you give to it","movements": [{"mirror": 41,"ud": 20,"lr": 20}, {"mirror": 42,"ud": 20,"lr": 20}, {"mirror": 44,"ud": 1,"lr": 10}]}'
    
def handleplayframe(msg):
    j = json.loads(msg)
    #print (j)
    for movement in j['movements']:
        routemovemirror(json.dumps(movement))
        print(movement)


def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code "+str(rc))
        client.subscribe(movemirror)
        client.subscribe(playframe)
    except Exception as e:
        client.publish("error", "router issue:"+str(e))
        #print("Exception: "+str(e))
    
def on_message(mqttc, obj, msg):
    try:
        print(msg.topic)
        payload = msg.payload.decode("utf-8")
        if msg.topic==movemirror:        
            routemovemirror(payload)
     
        if msg.topic==playframe:        
            handleplayframe(payload)
    except Exception as e:
        client.publish("error", "router issue:"+str(e))
        #print("Exception: "+str(e)





#startup code
client = mqtt.Client("router")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)
client.loop_forever()
