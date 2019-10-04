# Server for accelerator module for signal Reclection
# 2019 by MakerMatty


#mosquitto_pub -t movemirror -m '{"mirror":44,"ud":15.1,"lr":-25}'
import sys
import json
import paho.mqtt.client as mqtt
import time
import socket
import sys

#configurable variables
mqtt_broker_address = "10.25.249.104"
mqtt_broker_port    = 1883
#mqtt_topic = 'hub1/pinlevelapi'
server_host         = "10.25.249.143"
server_port         = 10000


def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code "+str(rc))
        client.subscribe(movemirror)
        client.subscribe(playframe)
    except Exception as e:
        client.publish("error", "router issue:"+str(e))
        #print("Exception: "+str(e))


client = mqtt.Client("acc_server")
client.on_connect = on_connect
#client.on_message = on_message
client.connect(mqtt_broker_address,port=mqtt_broker_port)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (server_host, server_port)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()


    try:
        print ('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            msg = data.decode("utf-8")

            #print('received "%s"' % data)
            #print('received "%s"' % msg)

            if data:
                #print('sending data back to the client')
                #connection.sendall(data)

                if msg[0] == 'x' or msg[0] == 'X':
                    val = msg[2:]
                    for i in range(0,16,2):
                        client.publish('hub1/pinlevelapi', '{"bonnet":0,"servo":'+str(i)+',"angle":'+str(val)+'}')

                elif msg[0] == 'y' or msg[0] == 'Y':
                    val = msg[2:]
                    for i in range(1,16,2):
                        client.publish('hub1/pinlevelapi', '{"bonnet":0,"servo":'+str(i)+',"angle":'+str(val)+'}')

            else:
                #print('no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
