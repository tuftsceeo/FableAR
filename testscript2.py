#Walker Wind
#testscript.py
#
#The following script is a test of controlling the fable robotics  using an outside python ide
#The script runs through a couple of movement commands that are separate from the current blockly.


#look into using a script where it does faster motor movements and uses math the calculate the 
#current angle at certain intervals and populates a list with this data. Each index of the list
#gets displayed in the AR in real time

import requests
import time

xPos=90 #ranging from 90 to -90
yPos=90 #ranging from 90 to -90
spd= 0 #speed constant (play with range based on motor speed capabilities
inGame=True


modname1=input("Please input the first module name:  ")
modname1= "'" + modname1 
modname1= modname1 + "'"
print("To exit, press the x button.")

xanglelist= []
yanglelist=[]
isModnameOne=True


def ChangePos(xPos,yPos, modname):
    command="api.setPos(" + str(xPos) + "," + str(yPos) + "," + modname + ")"
    r=requests.post("http://localhost:1234/run",data=command)

def pushCommand(command)
    r=requests.post("http://localhost:1234/run",data=command)

LeftArm = None
RightArm = None

commands=[]

def do_gymnastics():
  global LeftArm, RightArm
  commands.append("api.wait(1)")
  commands.append("api.setPos(0, 0, RightArm)")
  commands.append("api.setSpeed(50, 50, RightArm)")
#to do: finish wrapping the api commands, spots where the angle data is being read. Work on it tomorrow morning with
#lily to set it up well with thingworx 
  api.setPos(0, 0, LeftArm)
  api.setSpeed(50, 50, LeftArm)
  api.wait(1)
  api.setPos(90, 90, RightArm)
  api.setSpeed(50, 50, RightArm)
  api.setPos(-90, 90, LeftArm)
  api.setSpeed(50, 50, LeftArm)
  api.wait(1)
  api.setPos(0, 90, RightArm)
  api.setSpeed(50, 50, RightArm)
  api.setPos(0, 90, LeftArm)
  api.setSpeed(50, 50, LeftArm)
  api.wait(1)


def wave_hello():
  global LeftArm, RightArm
  api.setPos(0, 90, RightArm)
  api.setSpeed(50, 50, RightArm)
  api.wait(1)
  api.setPos(0, 0, RightArm)
  api.setSpeed(50, 50, RightArm)
  api.wait(1)


LeftArm = '6JC'
RightArm = '8JC'
while True:
  if api.isPressed('up'):
    do_gymnastics()
  elif api.isPressed('down'):
    wave_hello()
