# Capstone Drone DJ
For For ECE 4773 fall 2020
I am using this readme as a user guide to the software. 

## To set up the device please follow the softwareSetup.md documentation

This software is intended to run on a raspberry pi that is attached to a drone and it intends to analiyze the sound at different parts of a venue

# Start up
Before starting up your recorder make sure to place it on the stage or from your source of sound.

As soon as you power up the raspberry pi, the main.py script will play automatically.

The script will record the turn on location as the start location for calculations.

After this has happened you (the user) will have to find raspberry pi via wifi on a a laptop once found input password provided by set up team

now you may fly the drone to a desired location to test sound, once there press the button on the remote that came with your kit, play your test sound on your speakers, and wait for 3 minutes.

In the three minutes the sound has been recorded at the desired location.

Users may access the recordings and distance from their PC and analyze sound based off recording.

Users may repeat recordings or move to a new location and record

Recordings are saved by time and within each recording users will find:
  
  a recorded .wav file
  a csv with recording number, location of recording, and distance from origin point
  
When done simply turn off Raspberry Pi. 

When using drone again make sure to place infront of stage before starting up.
