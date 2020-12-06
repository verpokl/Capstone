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

spi = spidev.SpiDev()           # create the spi bus 
spi.open(0, 0)                  # open bus and chip select (bus, cs)

# Settings (for clock speed)
spi.max_speed_hz = 135000       # clk at 135 kHz for 75 ksps
# create the mcp object
# pull data from channel 7
# select pin is 8 or CE0
mcp = MCP3008(channel=7, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)

GPIO.setmode(GPIO.BCM)          # set up GPIO 13 as input
GPIO.setup(13,GPIO.IN)          # RF button pin 13 is input 

path = "/home/pi/archive/recordings/"       # location for all saved files

recordingNum = 0                            # number of recordings saved
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)        # set up gps daemon to run in the background
startLoc = getLocation()                    # save starting location for calculations

# main method ran automatically
def main():
    while 'true':                       # permanent loop ends when pi is shutdown
        if GPIO.input(13) == 1:         # if RF button activated
            location, distance = getLocation(startLoc)            # activate getLocation method that also calulates distance
            audio, samples = record(3)                             
            filecreation(location, distance, recordingNum, audio, sampleRate)
            recordingNum += 1
if __name__ == '__main__':
    main()

#-------------------------- additional methods
# pull data from channel 7
# general getlocation intended to create the starting location
def record(duration): # duration of recording in minutes
    start = time.time()                  # start timer
    rec = np.array([])                   # numpy array to hold recordings
    sec = 60 * duration;                 # convert duration to seconds
    while True:                          # while true record signals
        np.append(rec, mcp.value)        # append recent data to end of recording array
        if time.time() > start + sec : break    #end recording if time is up
    sampleRate = np.size(rec)/sec        # sample rate of recording is total record size/ time recording
    return x, sampleRate                 # return array with recording  
    
# creates new folder with stored input values
def filecreation(location, distance, recordingNum, audio, sampleRate):
    timestr = time.strftime("%Y%m%d-%H%M%S")                       # "yyyymmdd-hhmmss"
    os.mkdir(path, timestr)                                        # make path to /home/pi/archive/recordings/yyyymmdd-hhmmss
  
    with open(path + timestr + "/distance.csv", 'w', newline='') as file:     # create csv file and write in data values
        writer = csv.writer(file)                                    
        writer.writerow([recordingNum, location, distance])        # array with [recording number, location, and distance traveled]
    scale =  np.int16(audio/np.max(np.abs(audio)) * 32767)         # scaling audio recording data to convert to .wav
    write(path + timestr + "/audio.wav", sampleRate, scaled)        # write .wav file in directory

# general getlocation intended to create the starting location
def getLocation():
    # get gps coordinates from start location
    data = gpsd.next() 
    # verify gps data
    if loc['class'] == 'TPV':
        # pull gps data as [lon, lan]
        loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
        return loc
# getLocation that returns location and distance traveled startLocation from og constructor
def getLocation(startLoc):
                                                                  # get gps coordinates from start location
    data = gpsd.next() 
                                                                  # verify gps data
    if loc['class'] == 'TPV':
                                                                  # pull gps data as [lon, lan]
        loc = [getattr(loc,'lon'), 'unknown'], getattr(loc, 'lat', 'unknown')]
        time.sleep(1.0)                                           # wait one second to debounce switch
        return loc, mpu.haversine_distance(startLoc, loc)         # return [lon, lat], distance


spi.close()
