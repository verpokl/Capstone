# Outlining how to set up the raspberry pi software
For ECE 4773 fall 2020

## set up Raspi OS
Download Raspberry Pi OS with Raspberry Pi imager https://www.raspberrypi.org/software/
Load imager, choose SD card, and write (video instructions in link above)
Put SD card in RaspPi and power it up. 
Should be running Raspberry Pi OS

## Eanble SPI, SSH
Enable these options by going to preferences

Then select Raspberry Pi Configuration

Enable SPI and SSH

reboot

## Set up Samba to share files
### Install samba
```console
sudo apt-get update
sudo apt-get install samba samba-common-bin
```
### Create a shared directory
```console
sudo mkdir -m 1777 /share
sudo leafpad /etc/samba/smb.conf then add following to the end
```
```console
[share]
Comment = Pi shared folder
Path = /share
Browseable = yes
Writeable = Yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes
```
### create user and pass word for user
``` console
sudo smbpasswd -a pi
make password when prompted
sudo /etc/init.d/samba restart
```
## Install necessary repos for software to run
run following commands on command line after connecting powered pi to a monitor and a keyboard

### Update py3: 
```console
sudo apt update
sudo apt-get upgrade
```
### Install GPIO libraries: 
```console
pip3 install RPI.GPIO
sudo apt install python3-gpiozero
```
### Install circuitpython for busio: 
```console
pip3 install adafruit-blinka
```
### Install numpy for arrays: 
```console
sudo pip install numpy
```
### Install spidev: 
```console
sudo apt-get install python-dev python3-dev
cd ~
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
make
sudo make install
```
### Install GPSD: 
```console
sudo apt-get install gpsd gpsd-clients python-gps
```
### Install mpu:
``` console
sudo apt install python3-smbus
pip install mpu6050-raspberrypi
```
### Install scipy:
``` console
sudo apt-get install python3-scipy
```
### Install csv
``` console
pip install python-csv
```
## Install and run on startup main.py
download main.py on raspberry pi
run following command:
``` console
sudo python /home/pi/main.py &
```
will run on reboot
