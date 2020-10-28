## Main function.

#set up GPIO
recordingNum = 0
startLoc = getLocation('false')
while 'true':
    if buttonHit():
        location, distance = getLocation('true')
        audio, samples = record()
        filecreation(location, distance, recordingNum, audio, sampleRate)
        recordingNum += 1
