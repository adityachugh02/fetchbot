# Installation
This project has been tested on a Windows 10 64-bit machine and a Raspberry Pi 4.
## Raspberry Pi
Using Raspberry Pi Imager (https://www.raspberrypi.com/software/), install Raspberry Pi OS (Debian version 11: https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2022-04-07/2022-04-04-raspios-bullseye-armhf-full.img.xz)

Once the OS is loaded onto the SD card, connect a display, mouse and a keyboard to the Raspberry Pi. Start by configuring the basic preferences according to your region. 

After the configuration is complete, open a new terminal windows and enter:
> sudo raspi-config
### Enable Legacy Camera
Enable legacy camera in **Interface Options>Legacy Camera**.
### Enable SSH
Enable SSH in **Interface Options>SSH**.
### Auto Login
Enable Auto Login in **System Options>Boot/Auto Login>Console Auto Login**.
### Disable Wifi
Wifi and bluetooth tend to interfere because of their similar frequencies, it is recommended to disable the wifi while using bluetooth.
In the terminal enter:
> sudo ifconfig wlan0 down

### Install Python Packages
Connect the Raspberry Pi to the internet with ethernet.
It is recommended to use SSH ( with ethernet) for the following steps.

In the terminal, enter the following commands:
> sudo apt-get update

> sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

> pip install opencv-python==4.5.3.56

> pip install -U numpy

### Run Program at Startup


## Windows


