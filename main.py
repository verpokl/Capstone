## Main function.

#set up GPIO
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN) #button 

recordingNum = 0
startLoc = getLocation('false')

while 'true':
    # if rf button activated
    if GPIO.input(13) == 1:
        location, distance = getLocation('true')
        audio, samples = record()
        filecreation(location, distance, recordingNum, audio, sampleRate)
        recordingNum += 1
