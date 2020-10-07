# Capstone Drone DJ
For 2020 Capstone project 


Main Designated users are builders(us) and then clients (experienced sound engineers)
# Main steps of set up:
1.  Boot Raspberry Pi with Raspberry Pi OS
2.  Configure A to D pin and conncection for mic
3.  Set up recording
  3.1.  If cheaper model start recording sound as soon as user activates drone  
  3.2.  If mid tier model configure remote activation of recording 
  3.3.  If high tier model update user's computer with real time recording
4.  Analyzing recording 
  4.1.  If cheaper model, user brings in drone and connects to monitor or removes sd card to access recorded files
  4.2.  If mid tier model, user can access recordings in similar fashion but can record multiple at one time
  4.3.  If high tier model, user can see recordings on their computer as they are flying drones

# Raspberry Pi Stuff
## 0 and 4 stats
https://www.raspberrypi.org/products/raspberry-pi-zero-w/
pi 0 with wifi compatability
802.11 b/g/n wireless LAN
Bluetooth 4.1
Bluetooth Low Energy BLE

https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
pi 4 B
2.4 GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE

## OS link
https://www.raspberrypi.org/downloads/
link to download raspberry pi OS to flash drive also includes flashing software

## GPIOZERO is general GPIO library
https://gpiozero.readthedocs.io/en/stable/

# installing python
First, update your repositories list:
  
    pi@raspberrypi:~$ sudo apt update

Then install the package for Python 3:

    pi@raspberrypi:~$ sudo apt install python3-gpiozero

To use remote pins need pigpen

    $ sudo apt install pigpio
    
https://gpiozero.readthedocs.io/en/stable/remote_gpio.html



