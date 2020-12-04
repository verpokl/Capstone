## Main function.

import RPi.GPIO as GPIO
import time

# set up GPIO 13 as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN) # RF button pin 13 is input 

# number of recordings saved
recordingNum = 0
# save starting location for calculations
startLoc = getLocation()

while 'true':
    # if RF button activated
    if GPIO.input(13) == 1:
        # activate getLocation method that also calulates distance
        audio, samples = record()
        filecreation(location, distance, recordingNum, audio, sampleRate)
        recordingNum += 1
