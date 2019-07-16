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
modname2=input("Please input the second module name:  ")
modname1= "'" + modname1 
modname1= modname1 + "'" 
modname2="'" + modname2
modname2= modname2 + "'"
print("To exit, press the x button.")

xanglelist= []
yanglelist=[]
isModnameOne=True


def PosChange(xPos,yPos, modname):
    command="api.setPos(" + str(xPos) + "," + str(yPos) + "," + modname + ")"
    r=requests.post("http://localhost:1234/run",data=command)

delta=15
PosChange(0,0,modname1)
PosChange(0,0,modname2)

PosChange(0,30,modname1)
PosChange(0,-30,modname2)
PosChange(0,-30,modname1)
PosChange(0,30,modname2)
#while loop that runs separate movement functions

print("Currently taking user input. Each key press changes the angle by 15 deg.")
print("Module 1 uses wasd for movement, Module 2 uses ijkl")
while inGame==True:
    userinput=input()
#if the i key is pressed
    if userinput=='i':
        if yPos <=(90-delta):
            yPos=yPos+delta
            isModnameOne=True
        else:
            print("Error: Motor at position limit")

#if the k key is pressed
    if userinput=='k':
        if yPos >= (delta-90):
            yPos=yPos-delta
            isModnameOne=True
        else:
            print("Error: Motor at position limit")

#if the j key is pressed 
    if userinput=='j':
        if xPos >= (delta - 90):
            xPos=xPos-delta
            isModnameOne=True
        else:
            print("Error: Motor at position limit")
#if the l key is pressed 
    if userinput=='l':
        if xPos <= (90-delta):
            xPos=xPos+delta
            isModnameOne=True
        else:
            print("Error: Motor at position limit")
#if the w key is pressed
    if userinput=='w':
        if yPos <=85 :
            yPos=yPos+delta
            isModnameOne=False
        else:
            print("Error: Motor at position limit")
#if the s key is pressed 
    if userinput=='s':
        if yPos >= -85:
            yPos=yPos-delta
            isModnameOne=False
        else:
            print("Error: Motor at position limit")
#if the a key is pressed
    if userinput=='a':
        if xPos >= -85:
            xPos=xPos-5
            isModnameOne=False
        else:
            print("Error: Motor at position limit")
#if the d key is pressed
    if userinput=='d':
        if xPos <=(90-delta):
            xPos=xPos+delta
            isModnameOne=False
#if the x button is pressed
    if userinput=='x':
        inGame=False
        break
#update the angle (this is where the data will be transmitted to the cloud)
    xanglelist.append(xPos)
    yanglelist.append(yPos)
#change the angle
    if isModnameOne==True:
        PosChange(xPos,yPos,modname1)
    else:
        PosChange(xPos,yPos,modname2)


print('All Done!')



