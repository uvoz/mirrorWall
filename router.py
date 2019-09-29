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
mqtt_broker_port    =1884
movemirror          ='movemirror'
     
def routemovemirror(msg):
    j = json.loads(msg)
    address=mm.getMirrorAddress(j['mirror'])
    hub=address['hub']
    print("routing to hub "+str(hub)+": "+json.dumps(j))
    client.publish("hub"+str(hub)+"/"+movemirror,msg)



def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code "+str(rc))
        client.subscribe(movemirror)

    # beacuse otherwize we don't know whats wrong if something is
    except Exception as e:
        print("Exception: "+str(e))


    
def on_message(mqttc, obj, msg):
    try:
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        print("top="+topic+", pay="+payload)
        if topic==movemirror:
            routemovemirror(str(msg.payload))

    # beacuse otherwize we don't know whats wrong if something is
    except Exception as e:
        print("Exception: "+str(e))


#startup code
client = mqtt.Client("router")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)
client.loop_forever()
