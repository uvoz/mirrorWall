# ROUTER for mirror messages
# 2019 by StrejcekBob
# tested by MakerMatty
# This module is a central router that receives mirror movements, frames and animations
#it listens to messages sent to the movemirror topic, retrieves the hub address and forwards the message to the hub
#no validation is made her to keep it light. Validation is done distributed by all hubs.
#mosquitto_pub -t movemirror -m '{"mirror":44,"ud":15.1,"lr":-25}'

#mosquitto_pub -t movemirrornontranslated -m '{"mirror":44,"ud":15.1,"lr":-25}'

import mirrormap as mm
import sys
import json
import paho.mqtt.client as mqtt
import time

#declaration - idk if it is needed, but here it is
mqtt_broker_address = mqtt_broker_port = movemirror = movemirrornontranslated = playframe = playanimation = router = ""

#configurable variables
with open("config.json", 'r') as f:
    configdata = json.load(f)
    mqtt_broker_address     =str(configdata["mqtt_broker_address"])
    mqtt_broker_port        =int(configdata["mqtt_broker_port"])
    router                  ='router'
    movemirror              ='movmir'
    movemirrornontranslated ='movnon'
    playframe               ='playfr'
    playanimation           ='playan'
  

#mosquitto_pub -t movmir -m '{"mi":44,"ud":15.1,"lr":-25}'

def routemovemirror(msg):
    j = json.loads(msg)
    address=mm.getMirrorAddress(j['mi'])
    hub=address['hub']
    #print("routing to hub "+str(hub)+": "+json.dumps(j))
    client.publish("hub"+str(hub)+"/"+movemirror,msg)
    
    
#mosquitto_pub -t movnon -m '{"mi":44,"ud":100,"lr":25}'

def routemmovemirrornontranslated(msg):
    j = json.loads(msg)
    address=mm.getMirrorAddress(j['mi'])
    hub=address['hub']
    #print("routing untranslated to hub "+str(hub)+": "+json.dumps(j))
    client.publish("hub"+str(hub)+"/"+movemirrornontranslated,msg)


#mosquitto_pub -t playfr -m '{"pos":[{"mi":41,"ud":20,"lr":20},{"mi": 42,"ud":20,"lr":20},{"mi":44,"ud":1,"lr":10}]}'

def handleplayframe(msg):
    j = json.loads(msg)
    #print("handleplayframe invoked")
    #print (j)
    for movement in j['pos']:
        routemmovemirrornontranslated(json.dumps(movement))
        #print("movement seen")
        #print(movement)


'''
#mosquitto_pub -t playanimation -m '{"Animation": "some name you give to it","frames": [{"Frame": "some name you give to it","movements": [ {"mirror": 44,"ud": 1,"lr": 10}]}]}'

def handleplayanimation(msg):
    j = json.loads(msg)
    #print (j)
    for frame in j['frames']:
        handleplayframe(json.dumps(frame))
        #print("call handleplayfram>=:"+json.dumps(frame))
'''


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    try:          
        client.subscribe(movemirror)
        client.subscribe(movemirrornontranslated)
        client.subscribe(playframe)
        client.subscribe(playanimation)   
        
    except Exception as e:
        client.publish("error", router + " on_connect issue:"+str(e))


def on_message(mqttc, obj, msg):
    try:   
        #print(msg.topic)
        payload = msg.payload.decode("utf-8")      
        if msg.topic==movemirror:
            routemovemirror(payload)
        elif msg.topic==movemirrornontranslated:
            routemmovemirrornontranslated(payload)  
        elif msg.topic==playframe:      
            handleplayframe(payload)
        elif msg.topic==playanimation:
            handleplayanimation(payload)
            
    except Exception as e:
        client.publish("error", router + " on_message issue:"+str(e))
        

client = mqtt.Client(router)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)
client.loop_forever()
