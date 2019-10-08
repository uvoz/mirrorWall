# MQTT triggered communication to i2c Adafruit 16-Channel 12-bit PWM/Servo Bonnet
# 2019 by StrejcekBob
# tested by MakerMatty
# This are the interfaces between the outside word and the HUB.
# You talk to a hub by sending it MQTT messages.

# 1- remote control each servo separately. no translation=blind fast.
# Example mqtt message:
# mosquitto_pub -t hub1/pinlevelapi -m '{"bonnet":0,"servo":0,"angle":100}'
#topic (-t) is the hub you send the message to
#servo is the servo you like to move (0-15)
#angle is the target angle of the servo

# 2- remote control a mirror by sending it ud and lr positions.
# the mirror address is picked up in the mirror-map, the angles given in real degrees are translated in proper servo angles.
# this is very compute intensive so expect 8 frames/second for the entire mirror grid.
# Example mqtt message:
# mosquitto_pub -h 127.0.0.1 -t movemirror -m '{"mirror":44,"ud":20,"lr":20}'

import mirrormap as mm
import sys
import math
import json
import paho.mqtt.client as mqtt
import time
from adafruit_servokit import ServoKit

#@Petr:Also, can someone verify that UD;LR = 0°;0° mirror position is 82.12°;82.12°
UD_RelativeZero=82.12
LR_RelativeZero=82.12
#@Pert UD mirror angle transfered to UD servo rotation results results to 2D curve extruded over domain of mirror available movements <-30;30>
POLICE_MAX_ANGLE=30
POLICE_MIN_ANGLE=-30
#@Petr:The "policemen script" preventing servo from reaching dangerous angle should always keep it within <14.81;144.04> domain
POLICE_SERVO_MIN_SERVO_POS=16
POLICE_SERVO_MAX_SERVO_POS=142
#Matej: servo calibration
SERVO_PULSE_MIN=910
SERVO_PULSE_MAX=2260


#declaration - idk if it is needed, but here it is
mqtt_broker_address = mqtt_broker_port = hub = pinlevelapi = movemirror = movemirrornontranslated = ""

#configurable variables
with open("config.json", 'r') as f:
    configdata = json.load(f)
    mqtt_broker_address         =str(configdata["mqtt_broker_address"])
    mqtt_broker_port            =int(configdata["mqtt_broker_port"])
    hub                         =configdata["hub"]
    pinlevelapi                 =hub+'/pinlvl'
    movemirror                  =hub+'/movmir'
    movemirrornontranslated     =hub+'/movnon'
    
  

try:
    bonnets=[ServoKit(channels=16 , address=64),ServoKit(channels=16, address=65),ServoKit(channels=16, address=66)]
    for b in range(len(bonnets)):
        for i in range(16):
            bonnets[b].servo[i].set_pulse_width_range(SERVO_PULSE_MIN, SERVO_PULSE_MAX)

except:
    print("Problem with bonnets ?!:", sys.exc_info()[0])

#x =20#mirror UD in degrees from -30 to 30
#y =10#mirror LR in degrees from -30 to 30


def UDservo_poly(udangle):
    #starttime = int(round(time.time() * 1000))
    servoangle=(2.752e-12*udangle**8)+(1.701e-10*udangle**7)-(3.189e-09*udangle**6)-(4.918e-08*udangle**5)+(5.804e-07*udangle**4)+(0.0002402*udangle**3)-(0.002954*udangle**2)+(1.853*udangle)+(82.13)
    #endtime = int(round(time.time() * 1000))
    #print('UDservo_poly processing time:'+str(endtime-starttime))
    return round(servoangle,2)
    

def LRservo_poly (udangle, lrangle):
    #starttime = int(round(time.time() * 1000))
    servoangle=(82.15)+(1.4e-16*udangle)+(1.856*lrangle)+(0.000114*udangle**2)+(-5.438e-18*udangle*lrangle)+(-0.003402*lrangle**2)+(1.625e-18*udangle**3)+(-0.0002783*udangle**2*lrangle)+(-1.428e-18*udangle*lrangle**2)+(0.0001802*lrangle**3)+(-2.438e-07*udangle**4)+(1.728e-20*udangle**3*lrangle)+(5.568e-06*udangle**2*lrangle**2)+(2.203e-21*udangle*lrangle**3)+(4.473e-07*lrangle**4)+(-2.22e-21*udangle**5)+(3.245e-08*udangle**4*lrangle)+(1.969e-21*udangle**3*lrangle**2)+(-1.994e-07*udangle**2*lrangle**3)+(4.577e-22*udangle*lrangle**4)+(1.575e-07*lrangle**5)
    #endtime = int(round(time.time() * 1000))
    #print('LRservo_poly processing time:'+str(endtime-starttime))10. do 13. října 2019 na
    return round(servoangle,2)






#mosquitto_pub -t hub1/pinlvl -m '{"bo":0,"se":0,"an":100}'

def handlepinlevelapi(msg):
    #for x in range(10000):
    j = json.loads(msg)

    #print(j)
    if j['bo']<0 or j['bo']>2 or j['se']<0 or j['se']>15 or j['an']<POLICE_SERVO_MIN_SERVO_POS or j['an']>POLICE_SERVO_MAX_SERVO_POS:
        errormessage='handlepinlevelapi received invalid parameters:'+json.dumps(j)
        client.publish("error", errormessage)
        return
    bonnets[j['bo']].servo[j['se']].angle = j['an']



#mosquitto_pub -t hub1/movnon -m '{"mi":44,"ud":30,"lr":80}'

def handlemovemirrornontranslated(msg):

    j = json.loads(msg)

    #print ("movemirrornontranslated activated")
    #print(j)#pinlevelapi
    if j['lr']<POLICE_SERVO_MIN_SERVO_POS or j['lr']>POLICE_SERVO_MAX_SERVO_POS or j['ud']<POLICE_SERVO_MIN_SERVO_POS or j['ud']>POLICE_SERVO_MAX_SERVO_POS or j['mi']<0 or j['mi']>90:
        errormessage='movemirrornontranslated received invalid parameters:'+json.dumps(j)
        client.publish("error",errormessage)
        return
        
    address=mm.getMirrorAddress(j['mi'])

    newmsg={}
    newmsg['bo']=address['bonnet']
    newmsg['se']=address['UD-port']
    newmsg['an']=j['ud']

    handlepinlevelapi(json.dumps(newmsg, sort_keys=True))

    newmsg['se']=address['LR-port']
    newmsg['an']=j['lr']
    handlepinlevelapi(json.dumps(newmsg))



#mosquitto_pub -t hub1/movmir -m '{"mi":44,"ud":15.1,"lr":-25}'

def handlemovemirror(msg):

    j = json.loads(msg)

    if j['lr']<POLICE_MIN_ANGLE or j['lr']>POLICE_MAX_ANGLE or j['ud']<POLICE_MIN_ANGLE or j['ud']>POLICE_MAX_ANGLE or j['mi']<0 or j['mi']>90:
        errormessage='movemirror received invalid parameters: '+json.dumps(j)
        client.publish("error",errormessage)
        return
        
    address=mm.getMirrorAddress(j['mi'])

    newmsg={}
    newmsg['bo']=address['bonnet']
    newmsg['se']=address['UD-port']
    newmsg['an']=UDservo_poly(j['ud'])

    handlepinlevelapi(json.dumps(newmsg, sort_keys=True))

    newmsg['se']=address['LR-port']
    newmsg['an']=LRservo_poly(j['ud'],j['lr'])
    handlepinlevelapi(json.dumps(newmsg))




def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    try:      
        client.subscribe(pinlevelapi)
        client.subscribe(movemirror)
        client.subscribe(movemirrornontranslated)    

    # beacuse otherwize we don't know whats wrong if something is
    except Exception as e:
        #print("Exception: "+str(e))
        client.publish("error", hub+" on_connect issue:"+str(e))


def on_message(mqttc, obj, msg):
    try:
        payload = msg.payload.decode("utf-8")
        topic = msg.topic

        if topic==pinlevelapi:
            handlepinlevelapi(payload)
        elif topic==movemirror:
            handlemovemirror(payload)
        elif topic==movemirrornontranslated:
            handlemovemirrornontranslated(payload)

    # beacuse otherwize we don't know whats wrong if something is
    except Exception as e:
        #print("Exception: "+str(e))
        client.publish("error", hub+" on_message issue:"+str(e))


print(hub + " staring up...")
client = mqtt.Client(hub)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)


client.loop_forever()
