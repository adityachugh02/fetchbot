# Project Description
The Fetchbot interface allows users to connect to and control a Raspberry Pi based robot "Fetchbot", without internet connection. The connection between a computer and the robot is established through serial-over-bluetooth. 


![image](https://user-images.githubusercontent.com/60618118/187421842-e59810de-1c8c-49c3-9af5-bb2beb6852a1.png)
# Repository Structure
The Fetchbot interface is composed of 3 parts: The Blockly frame, the video/message frame and the AI Classifier frame.

Code for the Blockly frame can be viewed and edited in **/blockly/demos/code**.

New blocks need to be added in **fetchbot.js** and **displayed in index.html**.

Code for

# Installation
This project has been tested on a Windows 10 64-bit machine and a Raspberry Pi 4.
## Raspberry Pi
Using Raspberry Pi Imager (https://www.raspberrypi.com/software/), install Raspberry Pi OS full 32-bit (Debian version 11 (version is **not** default): https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2022-04-07/2022-04-04-raspios-bullseye-armhf-full.img.xz)

Once the OS is loaded onto the SD card, connect a display, mouse and a keyboard to the Raspberry Pi. Start by configuring the basic preferences according to your region. 

After the configuration is complete, open a new terminal window and enter:
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

### Clone Repository
Clone the project repository by entering the following in the terminal:
> git clone https://github.com/adityachugh02/fetchbot/

### Install Python Packages
Connect the Raspberry Pi to the internet with ethernet.
It is recommended to use SSH (with ethernet) for the following steps.

In the terminal, enter the following commands:
> sudo apt-get update

> sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

> cd fetchbot

> pip install -r requirements.txt

> pip install -U numpy

## Windows
Download the recommended Windows installer for Python 3 from: https://www.python.org/downloads/windows/.

Navigate to https://github.com/adityachugh02/fetchbot/ and click on **code>Download ZIP**. Extract the files once the download is complete.

**Or** if git is installed on Windows, in the command prompt enter:

> git clone https://github.com/adityachugh02/fetchbot/

### Install Python Packages

In the command prompt, enter the following commands:

> cd fetchbot

> pip install -r requirements.txt

# Bluetooth Setup
To enable serial communication over bluetooth, in the terminal on the Raspberry Pi enter:
> sudo nano /etc/systemd/system/dbus-org.bluez.service

Replace the line starting with **ExecStart=** with:

> ExecStart=/usr/lib/bluetooth/bluetoothd --compat --noplugin=sap
> ExecStartPost=/usr/bin/sdptool add SP

Save and exit the file with CTRL+X.

Restart the bluetooth service with:
> sudo systemctl daemon-reload;

> sudo systemctl restart bluetooth.service;

### Pairing
Still in the Rasberry Pi terminal, enter:
> sudo bluetoothctl

In bluetoothctl, enter:

> discoverable on

> pairable on

On your **Windows PC** go to **Settings>Devices>Bluetooth and other devices** and turn Bluetooth on. Next, click on **Add Bluetooth or other device** and select Bluetooth. A device named "Raspberry Pi" should appear.

Connect to the device and confirm the security code.

In the Raspberry Pi bluetoothctl, accept the service authorisation requests and enter:

> trust XX:XX:XX:XX:XX:XX

(Where XX:XX:XX:XX:XX:XX is the MAC Adress of the Windows PC.)

And exit bluetoothctl:
> exit

If you are using multiple bluetooth devices together, a unique channel needs to be assigned to each Raspberry Pi.

In this case, enter:
> sudo rfcomm release all

> sudo rfcomm bind /dev/rfcomm1 XX:XX:XX:XX:XX:XX <CHANNEL NUMBER>

By default, the Raspberry Pi is configured as an audio device which means that some services can be disabled. On On your **Windows PC** go to **Settings>Devices>Bluetooth and other devices**, on the right, click on **Devices and printers**. While the bluetooth connection is active, right-click the Raspberry Pi and select **Properties**. In the **Properties** window, select **services** and deselect all checkboxes except **Audio Sink** (without this services the connection hangs) and **Serial Port (SPP)**.

Finally, make a note of the **COM port number**.

# Execution
## Windows
On your **Windows PC**, navigate to **preferences.txt** in the fetchbot folder. Replace the **COM port number** with the one noted. Save and exit the file.

The program can be executed by double-clicking **start.sh** or from the command prompt with:
> python3 main.py

## Raspberry Pi
For the program not to interfere with the startup processes, it is best the run the program once the startup is complete at auto login.

In the Raspberry Pi terminal, enter:
> nano /home/pi/.bashrc

Add this line at the end of the file:
> python /home/pi/fetchbot-rpi/main.py

Save and exit the file with CTRL+X.

Now the program should run automatically when the Raspberry Pi is powered.

# Notes
Make sure that the bluetooth connection is active between the Raspberry Pi and the Windows PC before launching the program on the Windows PC. (The Raspberry Pi is ready for connection when the green led (pin 14) of the motor shield turns on.)
