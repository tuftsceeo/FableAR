#Walker Wind
#testscript.py
#
#The following script is a test of using thingworx  using an outside python ide
#The script runs through a couple of movement commands that are separate from the current blockly.


#Using the example "follow the leader"
#the angle is  of the leader is being dictated
#and is sent to the follower which moves to the same position
#there are points marked in the script where data can be sent to the thingworx
#server and then sent to the AR 

import requests, time, keyboard, json



#function that changes the position
def ChangePos(xPos,yPos, modname):
    command="api.setPos(" + str(xPos) + "," + str(yPos) + ",'" + modname + "')"
    r=requests.post("http://localhost:1234/run",data=command)

#function if given a command to post
def postCommand(command):
    r=requests.post("http://localhost:1234/run",data=command)
    return r

#function that does a get Command
def getCommand(command):
    datum=requests.get("http://localhost:1234/run",data=command)
    return datum

#function that reads variables to Thingworx
def readtoThingworx(propName1,propName2,propValue1,propValue2):
	payload = {propName1:propValue1, propName2:propValue2}
    url= "https://ptcacademic-dev3-twx.es.thingworx.com/Thingworx/Things/FableARData/properties"
	headers = {'appKey': "9e2960df-5b7c-476c-8b60-3d9b77037a28", 'Accept': "application/json",'Content-Type':"application/json"}
    
    putResponse = requests.put(url + '*',headers=headers,json=payload)
    print(putResponse.status_code)

    getResponse = requests.get(url+'/'+propName1,headers=headers)
    print(getResponse.status_code)

    text = getResponse.text
    json = json.loads(text)
    rows = json.get('rows')
    namevalue = rows[0][propName1]
    print(namevalue)

Leader = None
Follower = None
starttime=0
currenttime=0

xpos=0
ypos=0
Leader = '6JC'
Follower = '8JC'
propName1='xpos'
propName2='ypos'
propValue1='0'
propValue2='0'

ChangePos(xpos,ypos,'6JC')
while True:
   

    if keyboard.is_pressed('up') == True:
        ypos+=15
    if keyboard.is_pressed('down') == True:
        ypos=ypos-15
    if keyboard.is_pressed('left') == True:
        xpos+=15
    if keyboard.is_pressed('right') == True:
        xpos=xpos-15
   
    propValue1=str(xpos)
    propValue2=str(ypos)
    
    #calls the function to send the data to the Thingworx server
    readtoThingworx(propName1,propName2,propValue1,propValue2)
    
    #timer surrounds the post command to see how fast it takes to run the command
    starttime=time.time()
    ChangePos(xpos,ypos,'6JC')
    currenttime=time.time()
    delta=currenttime-starttime
    print("{:f}".format(delta))
