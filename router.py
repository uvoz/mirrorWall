# ROUTER for mirror messages
# 2019 by StrejcekBob
# Upgraded by MakerMatty
# Tested by MakerMatty
# This module is a central router that receives mirror movements, frames and animations
#it listens to messages sent to the movemirror topic, retrieves the hub address and forwards the message to the hub
#no validation is made her to keep it light. Validation is done distributed by all hubs.

import mirrormap as mm
import sys
import json
import paho.mqtt.client as mqtt
import time

#declaration - idk if it is needed, but here it is
mqtt_broker_address = mqtt_broker_port = movemirror = moveservos = playframe = playframe_raw = playanimation = router = calibrate = ""

#configurable variables
with open("config.json", 'r') as f:
    configdata = json.load(f)
    mqtt_broker_address     =str(configdata["mqtt_broker_address"])
    mqtt_broker_port        =int(configdata["mqtt_broker_port"])
    router                  ='router'
    movemirror              ='movmir'
    moveservos              ='movser'
    calibrate               ='calibr'
    playframe               ='playfr'
    playframe_raw           ='playfr_raw'
    #playanimation          ='playan'
  
  

#mosquitto_pub -t movmir -m '{"mi":44,"ud":15.1,"lr":-25}'

def routeMoveMirror(msg):
    j = json.loads(msg)   

    msg={}   
    msg["mi"]=mm.getMirrorHubAddress(j["mi"])
    msg["ud"]=j["ud"]
    msg["lr"]=j["lr"]
       
    t="hub"+str(mm.getHubNumber(j['mi']))+"/"+movemirror
    p=json.dumps(msg)
    
    client.publish(t,p)
    
    
#mosquitto_pub -t movser -m '{"mi":44,"ud":100,"lr":25}'

def routeMoveServos(msg):
    j = json.loads(msg)   

    msg={}   
    msg["mi"]=mm.getMirrorHubAddress(j["mi"])
    msg["ud"]=j["ud"]
    msg["lr"]=j["lr"]
       
    t="hub"+str(mm.getHubNumber(j['mi']))+"/"+moveservos
    p=json.dumps(msg)
    
    client.publish(t,p)


#mosquitto_pub -t hub1/calibr -m '{"mi":0,"dud":-0.1,"dlr":1.2}'

def routeCalibrate(msg):
    j = json.loads(msg)   

    msg={}   
    msg["mi"]=mm.getMirrorHubAddress(j["mi"])
    msg["dud"]=j["dud"]
    msg["dlr"]=j["dlr"]
       
    t="hub"+str(mm.getHubNumber(j['mi']))+"/"+calibrate
    p=json.dumps(msg)
    
    client.publish(t,p)


#mosquitto_pub -t playfr -m '{"pos":[{"mi":41,"ud":20,"lr":20},{"mi": 42,"ud":20,"lr":20},{"mi":44,"ud":1,"lr":10}]}'

def handlePlayFrame(msg):
    j = json.loads(msg)
    #print("handlePlayFrame invoked")
    #print (j)
    for movement in j['pos']:
        routeMoveServos(json.dumps(movement))
        #print("movement seen")
        #print(movement)


#mosquitto_pub -t playfr_raw -m '50.0;21.11;33;14;50.0;21.11'     # 'up0;lr0;up1;lr1; ... ;up90;lr90'

def handlePlayFrameRaw(s):
    #CSV format
    s.split(';')
    
    for i in range(0, len(s), 2):
        mov = {}
        mov['mi'] = i//2
        mov['ud'] = float(s[i])
        mov['lr'] = float(s[i+1])
        routeMoveServos(json.dumps(mov))

'''
#mosquitto_pub -t playanimation -m '{"Animation": "some name you give to it","frames": [{"Frame": "some name you give to it","movements": [ {"mirror": 44,"ud": 1,"lr": 10}]}]}'

def handlePlayAnimation(msg):
    j = json.loads(msg)
    #print (j)
    for frame in j['frames']:
        handlePlayFrame(json.dumps(frame))
        #print("call handleplayfram>=:"+json.dumps(frame))
'''


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    try:       
        #client.subscribe(topic,QoS)
        client.subscribe(movemirror,0)
        client.subscribe(moveservos,0)
        client.subscribe(playframe,0)
        client.subscribe(playframe_raw,0)
        #client.subscribe(playanimation,0)   
        client.subscribe(calibrate,1) 
        
    except Exception as e:
        client.publish("error", router + " on_connect issue:"+str(e))


def on_message(mqttc, obj, msg):
    try:   
        #print(msg.topic)
        payload = msg.payload.decode("utf-8")      
        if msg.topic==movemirror:
            routeMoveMirror(payload)
        elif msg.topic==moveservos:
            routeMoveServos(payload)  
        elif msg.topic==calibrate:
            routeCalibrate(payload)
        elif msg.topic==playframe:      
            handlePlayFrame(payload)
        elif msg.topic==playframe_raw:
            handlePlayFrameRaw(payload)
        #elif msg.topic==playanimation:
        #    handlePlayAnimation(payload)

            
    except Exception as e:
        client.publish("error", router + " on_message issue:"+str(e))
        

client = mqtt.Client(router)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)
client.loop_forever()
