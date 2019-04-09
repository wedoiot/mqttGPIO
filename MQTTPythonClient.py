#!/usr/bin/python
import paho.mqtt.client as mqtt
import OPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, 0)             

def on_connect(self,mosq, obj, rc):
    print("rc: " + str(rc))
    a= client.subscribe("test",0)
    print("result: " + str(a))
    print("se suscribio a test")

    
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)   
    if (str(message.payload.decode("utf-8"))=="ON"):
        print("led ON") 
        GPIO.output(5, 1) 
    elif (str(message.payload.decode("utf-8"))=="OFF"):
        print("led OFF") 
        GPIO.output(5, 0)   

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)
    
client = mqtt.Client()

# Assign event callbacks
client.on_connect   = on_connect 
client.on_message   = on_message
client.on_subscribe = on_subscribe
client.on_publish   = on_publish
# Assign credentials
client.username_pw_set(username="wedoiot",password="Plamontina01")
# Connect
client.connect("192.168.1.4", 1883, 60)

try:
    while(1):
        #check new data
        client.loop_forever() 

except KeyboardInterrupt:
    GPIO.output(5, 0)           # set port/pin value to 0/LOW/False
    GPIO.cleanup()              # Clean GPIO
    print ("Bye.")

