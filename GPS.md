# Setting up GPS on raspberry pi
all pulled from https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4

First of all wire up correctly with vcc, TX and RX swapped on the raspberry pi

## Next need to configure pi for gps do by:

sudo raspi-config 
type the above in command line, this opens a window.
 select “Interfacing Options” and then “Serial”
 disable the possibility to access the login-shell via a serial connection and in the next step, 
 choose “Yes” when you get asked whether you want the serial ports to remain enabled
 choose “Finish” and then reboot the Raspberry Pi.
 
## Need to install gpsd and the gpsd-client:

sudo apt-get install gpsd gpsd-clients
man gpsd

when installation complete verify getting data from serial
cat /dev/serial0

verify you are admin/super user by running following
sudo adduser pi dialout

## Reading position data:

sudo systemctl stop gpsd.socket
stops gpsd to set correctly for pi
 
Note that you’ll have to type this command every time you boot up the system. Alternatively, you can also disable it entirely:     
sudo systemctl disable gpsd.socket

Start a new gpsd instance that redirects the data of the correct serial port to a socket:
sudo gpsd /dev/serial0 -F /var/run/gpsd.sock

can run either of the following two commands to display the GPS data:
sudo gpsmon
sudo cgps -s

## can try the following instead
https://www.rhydolabz.com/wiki/?p=9557

https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all

https://area-51.blog/2012/06/18/getting-gps-to-work-on-a-raspberry-pi/   has a cool map we might be able to use
