# Capstone Drone DJ
For 2020 Capstone project 


Main Designated users are builders(us) and then clients (experienced sound engineers)
# Main steps of set up:
1.  Boot Raspberry Pi with Raspberry Pi OS
2.  Install arduino and set up MULTIWII to control motors
3.  Calibrate motors and sensors
4.  Set up controller
  4.1.  Create and conncect to DHCP server for app controlled and wifi connected drone
  4.2.  Connect to remote antenae control if not using app
5.  Install drone software
6.  Configure A to D pin and conncection for mic
7.  Set up recording
  7.1.  If cheaper model start recording sound as soon as user activates drone  
  7.2.  If mid tier model configure remote activation of recording 
  7.3.  If high tier model update user's computer with real time recording
8.  Analyzing recording 
  8.1.  If cheaper model, user brings in drone and connects to monitor or removes sd card to access recorded files
  8.2.  If mid tier model, user can access recordings in similar fashion but can record multiple at one time
  8.3.  If high tier model, user can see recordings on their computer as they are flying drones

# Use Case For Setting up Controllers
|Use case name|Setting up Controllers|
------------|-------------
|Related requirements      |Antenae or Wifi connection to flight controll module
|Goal        |To allow users to controll the drone
|Preconditions|The drone be on and connected to a control system
|Succesful End Condition|A user is free to fly the drone effortlessly
|Failed End Condition|Drone not responding to flight commands
|Primary Actors|Sound engineers
|Secondary Actors|Builders troubleshooting
|Trigger|On turn on and connection to controller

|Main FLow|Step|Action|
------------|-------------|-------------
||1|The user activates drone and controller
||2|The user connects to drone and is able to move drone around
||2.1A|User connected via app and phone, able to press specific button to activate recording
||2.1B|User connected via remote controller, mainly used to fly can record initially or automatically with other remote
||3|The user turns off both when done operating


# Use Case For Recording Data
|Use case name|Recording Data|
------------|-------------
|Related requirements      |Antenae or Wifi connection to flight controll module 
|Goal        |To allow users to record data 
|Preconditions|The drone be on and connected to a control system
|Succesful End Condition|A user able to record the desired sound
|Failed End Condition|Recording weak or unintelligible
|Primary Actors|Sound engineers
|Secondary Actors|Builders troubleshooting
|Trigger|On turn on, or when button activated via remote

|Main FLow|Step|Action|
------------|-------------|-------------
||1|The user activates the drone
||1.1A|Drone may record as soon as activated and stops recording when deactivated
||2|User may also fly to desired destination and remotely activate recording
||2.1A|User May access data live if connected to internet


# Use Case For Analyzing Data
|Use case name|Analysing Data|
------------|-------------
|Related requirements      |User accesing recordings via internet or file system
|Goal        |To allow users to see the analysis of data
|Preconditions|The drone have or be recording data
|Succesful End Condition|Amplitude of signal and phase be displayed while filtering out drone's sounds
|Failed End Condition|Recording unintelligible and analysis unreliable
|Primary Actors|Sound engineers
|Secondary Actors|Builders troubleshooting
|Trigger|Accessed via file system or through internet connection

|Main FLow|Step|Action|
------------|-------------|-------------
||1.1A|The user might see live data being recorded through server connection
||1.1B|If no server connection, user may fly drone nearby and access files directly on drone


