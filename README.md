# mirrorWall
This is the software that flows messages to the mirror wall.
It lives on mosquitto MQTT.

# Todo: 

1. parse entire animations and submit each frame to the playframe handler.



# How to use from the outside:
## Move a mirror using translation of angles to servo angles: 

 mosquitto_pub -h 127.0.0.1 -t movemirror -m '{"mirror":44,"ud":20,"lr":20}'
 

## play a frame containing multiple/all mirror positions (using translation of angles above)
 
 #mosquitto_pub -t playframe -m '{"Frame": "some name you give to the frame","movements": [{"mirror": 41,"ud": 20,"lr": 20}, {"mirror": 42,"ud": 20,"lr": 20}, {"mirror": 44,"ud": 1,"lr": 10}]}'
 


## Move a servo on a bonnet connected to a hub (no servo angle translation):

 mosquitto_pub -t hub1/pinlevelapi -m '{"bonnet":0,"servo":0,"angle":140}'
 



