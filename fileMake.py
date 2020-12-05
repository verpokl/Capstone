import os
# time needed 
# numpy needed
from scipy.io.wavfile import write
import csv

path = "/home/pi/archive/recordings/"

def filecreation(location, distance, recordingNum, audio, sampleRate):
  timestr = time.strftime("%Y%m%d-%H%M%S")                       # "yyyymmdd-hhmmss"
  os.mkdir(path, timestr)                                        # make path to /home/pi/archive/recordings/yyyymmdd-hhmmss
  writ = [recordingNum, location, distance]                      # array with [recording number, location, and distance traveled]
  
  with open(path + timestr + "/distance.csv", 'w', newline='') as file:     # create csv file and write in data values
    writer = csv.writer(file)                                    
    writer.writerow(["SN", "Name", "Contribution"])
  scale =  np.int16(audio/np.max(np.abs(audio)) * 32767)         # scaling audio recording data to convert to .wav
  write(path + timestr + "/audio.wav", sampleRate, scaled)        # write .wav file in directory
