## Main function.
import busio
from gpiozero import MCP3008
import spidev
import numpy as np
import RPi.GPIO as GPIO
from gps import *
import time
import mpu
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
            audio, samples = record()
            filecreation(location, distance, recordingNum, audio, sampleRate)
            recordingNum += 1
if __name__ == '__main__':
    main()
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
