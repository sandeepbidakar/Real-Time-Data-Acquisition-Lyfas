import paho.mqtt.client as mqtt
from numpy import random
import matplotlib.pyplot as plt
import time
import paho.mqtt.subscribe as subscribe
import sys
import json
from matplotlib import style 
import matplotlib.animation as anim
import numpy as np


def on_connect(mqttc,obj,flags,rc):
    print("rc:" + str(rc))
def on_message(mqttc,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
def on_publish(mqttc,obj,mid):
    print("mid" + str(mid))
    pass
def on_subscribe(mqttc,obj,mid,granted_qos):
    print("Subscribe:" + str(mid)+" "+str(granted_qos))
global x
global y

x=[]
y=[]

def print_msg(client,userdata,message):
    parsed = json.loads(message.payload)
    a=str(parsed['d']['PULSE_RATE'])
    a=int(a)
    x.append(a)
    non_zeros=list(filter(lambda i: i!=0, x))
    print(non_zeros)
    c=np.mean(non_zeros)
    print(c)
    if c>=100:
        print("Abnormal Pulse Rate")
    else:
        print("Pulse Rate is Normal")
    print(hi)
    plt.ion()
    plt.plot(non_zeros)
    plt.pause(.05)
plt.show() 
           
def on_log(mqttc,obj,level,string):
    print(string)  
mqttc=mqtt.Client()
mqttc.on_connect=on_connect 
mqttc.on_message=on_message
mqttc.on_subscribe=on_subscribe
mqttc.on_log=on_log
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()
(mid,granted_qos)=subscribe.callback(print_msg,"Lyfas",hostname="iot.eclipse.org")
mqttc.loop_stop()
