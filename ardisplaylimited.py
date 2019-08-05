#ardisplaylimited.py



#Walker Wind
#demonstrating the limited functionality of the robot, but with a full AR experience: 
#
#libraries needed: numpy, time, keyboard, json, requests, math
#This script uses a couple of functions to move the fable Joint module by a certain
#angle increment. Due to the timing of requests, it runs slowly and takes a while to process
#each command request. 

#In the loop, the code is checking for a keyboard input (up,down,left,right) to move the
#position of the motors. The ChangePos function takes about 1.5 seconds and the 
#getState function takes about 1 second. The data from getState is sent to Thingworx, 
#which holds the data and allows it to be viewed using the Vuforia View app.




import requests, time, keyboard, json, math
from numpy import interp



#function that changes the position, given x and y position, module name, and session
def ChangePos(xPos,yPos, modname,session):
    command="api.setPos(" + str(xpos) + "," + str(ypos) + ",'" + modname + "')"
    session.post("http://localhost:1234/run",data=command) 

#function that can set the speed of the movements
def ChangeSpeed(xSpd,ySpd, modname, session):
    command="api.setSpeed(" + str(xSpd) + "," + str(ySpd) + ",'" + modname + "')"
    session.post("http://localhost:1234/run",data=command) 
   
#function that does a get Command given a session (note that the module ID should be changed for different modules)

def getState(session):
    re=session.get("http://localhost:1234/module_state", params={'mID':'6JC','mType':'JointManager'} )
    return re

#function that reads variables to Thingworx
def readtoThingworx(propName1,propName2,propValue1,propValue2,session):
    payload = {propName1:propValue1, propName2:propValue2}
    url= "https://ptcacademic-dev3-twx.es.thingworx.com/Thingworx/Things/FableARData/Properties/"
    headers = {'appKey': "9e2960df-5b7c-476c-8b60-3d9b77037a28", 'Accept': "application/json",'Content-Type':"application/json"}
    
    putResponse = session.put(url + '*',headers=headers,json=payload)
    #print("the put response is", putResponse.status_code)

    getResponse = session.get(url+'/'+propName1,headers=headers)
    #print("the get response is ",getResponse.status_code)

    text = getResponse.text
    json1 = json.loads(text)
    rows = json1.get('rows')
    namevalue = rows[0][propName1]
    #print("the x value is ", namevalue)

def mapper(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def detectkeyinput(xpos,ypos,is_broke):

    if keyboard.is_pressed('up') == True and ypos<= (90-movedelta):
        ypos+=movedelta
    if keyboard.is_pressed('down') == True and ypos >= (movedelta-90):
        ypos=ypos-movedelta
    if keyboard.is_pressed('left') == True and xpos <= (90-movedelta):
        xpos+=movedelta
    if keyboard.is_pressed('right') == True and xpos >= (movedelta-90):
        xpos=xpos-movedelta
    if keyboard.is_pressed('x') == True:
        print("Exiting program")
        is_broke=True
    return xpos, ypos, is_broke   

def PrintAngle(state):
    statedict=json.loads(state.text)
    xang=statedict['posX']['val']
    yang=statedict['posY']['val']
    currentxang= statedict['posX']['val']
    currentyang= statedict['posX']['val']
    xang=math.ceil(mapper(xang,205,819,-90,90))
    yang=math.ceil(mapper(yang,205,819,-90,90))
    print("Angle of X is {:f}".format(xang))
    print("Angle of Y is {:f}".format(yang))
    return xang, yang

starttime=0
currenttime=0

xpos=0
ypos=0
xspd=65
yspd= 65
movedelta=30
propName1='xangle'
propName2='yangle'
propValue1=44
propValue2=45
is_broke=False

#begin a session 
session=requests.Session()

starttime=time.time()

ChangeSpeed(xspd,yspd,'6JC',session)

currenttime=time.time()
delta=currenttime-starttime
print("Timer for ChangeSpeed is {:f}".format(delta))

while is_broke==False:
   
    #checking for keyboard input
    xpos, ypos, is_broke = detectkeyinput(xpos, ypos, is_broke)

    #timing the ChangePos function on module '6JC'
    starttime = time.time()
    ChangePos(xpos,ypos,'6JC',session)
    currenttime=time.time()
    delta = currenttime - starttime
    print("Timer for ChangePos is {:f}".format(delta))

    #Timing the getState function, returns the state
    starttime=time.time()
    state= getState(session) 
    xang, yang = PrintAngle(state)
    currenttime=time.time()
    delta=currenttime-starttime
    print("Timer for getState is {:f}".format(delta))

    starttime=time.time()
    #calls the function to send the data to the Thingworx server
    propValue1=str(xang)
    propValue2=str(yang)
    readtoThingworx(propName1,propName2,propValue1,propValue2,session)
    currenttime=time.time()
    delta=currenttime-starttime
    print("Timer for thingworx is {:f}".format(delta))

