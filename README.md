# mirrorWall
This is the software that flows messages to the mirror wall.
It lives on mosquitto MQTT.


## Todo: ##
1. parse frames and submit the positions trough messages to the hubs useing the existing mechanism.
2. parse animations and submit each frame to the new function above.



## How to use from the outside: ##
- Move a mirror using translation of angles to servo angles:
 mosquitto_pub -h 127.0.0.1 -t movemirror -m '{"mirror":44,"ud":20,"lr":20}'

- Move a servo on a bonnet connected to a hub :
 mosquitto_pub -t hub1/pinlevelapi -m '{"bonnet":0,"servo":0,"angle":140}'



2.
