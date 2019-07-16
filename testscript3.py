#Walker Wind
#testscript.py
#
#The following script is a test of controlling the fable robotics  using an outside python ide
#The script runs through a couple of movement commands that are separate from the current blockly.


#Using the example "follow the leader"
#the angle is  of the leader is being read
#and is sent to the follower which moves to the same position
#there are points marked in the script where data can be sent to the thingworx
#server and then sent to the AR 

import requests
import time

#print("To exit, press the x button.")

#def ChangePos(xPos,yPos, modname):
#    command="api.setPos(" + str(xPos) + "," + str(yPos) + "," + modname + ")"
#    r=requests.post("http://localhost:1234/run",data=command)

def postCommand(command):
    r=requests.post("http://localhost:1234/run",data=command)
    return r
def getCommand(command):
    datum=requests.get("http://localhost:1234/run",data=command)
    return datum

Leader = None
Follower = None

xangle=0
yangle=0
Leader = '6JC'
Follower = '8JC'
while True:
    if api.isPressed('up') == True:
        xpos+=1
    command="api.readJointSensor('angleX', Leader)"
   #this neeeds to be different xangle=postCommand(command)
    print(xangle.content)
    command="api.readJointSensor('angleY', Leader)"
    #this needs to be different yangle=postCommand(command)
    #This is where the xangle, yangle variables would be pushed to the thingworx server
    #it would live display the angle in ar 
    command = "api.setPos(xangle, yangle, Follower)"
    postCommand(command)
    command = "api.setSpeed(50, 50, Follower)"
    postCommand(command)
    
