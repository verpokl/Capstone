## Main function.
import busio
from gpiozero import MCP3008
import spidev
import numpy as np
import RPi.GPIO as GPIO
from gps import *
import time
import mpu
import os
from scipy.io.wavfile import write
import csv

# create the spi bus open bus and cs (bus, cs)
# clk at 135 kHz for 75 ksps
spi = spidev.SpiDev()
spi.open(0, 0)
p = pyaudio.PyAudio()

# Settings (for clock speed)
spi.max_speed_hz = 135000

# create the mcp object
# pull data from channel 7
# select pin is 8 or CE0
mcp = MCP3008(channel=7, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
# set up GPIO 13 as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN) # RF button pin 13 is input 
path = "/home/pi/archive/recordings/"

# number of recordings saved
recordingNum = 0
# save starting location for calculations
startLoc = getLocation()

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
def main():
    while 'true':
         # if RF button activated
        if GPIO.input(13) == 1:
            # activate getLocation method that also calulates distance
            location, distance = getLocation(startLoc)
            audio, samples = record()
            filecreation(location, distance, recordingNum, audio, sampleRate)
            recordingNum += 1
if __name__ == '__main__':
    main()

def filecreation(location, distance, recordingNum, audio, sampleRate):
  timestr = time.strftime("%Y%m%d-%H%M%S")                       # "yyyymmdd-hhmmss"
  os.mkdir(path, timestr)                                        # make path to /home/pi/archive/recordings/yyyymmdd-hhmmss
  writ = [recordingNum, location, distance]                      # array with [recording number, location, and distance traveled]
  
  with open(path + timestr + "/distance.csv", 'w', newline='') as file:     # create csv file and write in data values
    writer = csv.writer(file)                                    
    writer.writerow(["SN", "Name", "Contribution"])
  scale =  np.int16(audio/np.max(np.abs(audio)) * 32767)         # scaling audio recording data to convert to .wav
  write(path + timestr + "/audio.wav", sampleRate, scaled)        # write .wav file in directory

# general getlocation intended to create the starting location
def getLocation(gps):
    # get gps coordinates from start location
    data = gps.next() 
    # verify gps data
    if loc['class'] == 'TPV':
        # pull gps data as [lon, lan]
        loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
        return loc
# getLocation that returns location and distance traveled startLocation from og constructor
def getLocation(gps, startLoc):
    # get gps coordinates from start location
    data = gps.next() 
    # verify gps data
    if loc['class'] == 'TPV':
        # pull gps data as [lon, lan]
        loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
        # return [lon, lat], distance
        time.sleep(1.0) # wait one second to debounce switch
        return loc, mpu.haversine_distance(startLoc, loc) 

# pull data from channel 7
# general getlocation intended to create the starting location
def record(duration): # duration of recording in minutes
    start = time.time()         # start timer
    rec = np.array([])
    sec = 60 * duration;        # convert duration to seconds
    while True:                 # while true record signals
        np.append(rec, mcp.value)
        if time.time() > start + sec : break
    sampleRate = np.size(rec)/sec   #sample rate of recording 
    return x, sampleRate        # return array with recording
spi.close()
