import cv2
import serial
import time
import numpy as np
import base64
import motor_control
import os
import subprocess as sp

def connect():
    
    global ser
    
    if ser == None:
        try:
            os.system("sudo rfcomm listen rfcomm0 &")
            ser = serial.Serial("/dev/rfcomm0", timeout=0, baudrate=115000)
            print("Connected")
            return
        except:
            print("No connection")
            time.sleep(1)
    
    else:
        try:
            ser.close()
            ser = None
            print("Disconnecting, reconnecting...")
            time.sleep(1)
        except:
            print("Error")
            time.sleep(1)

motor_control.ready()

while len(sp.getoutput("hcitool con")) <= 12:
    pass

camera_object = cv2.VideoCapture(0)
ser = None

while True:
    try:
        
        ret, picture = camera_object.read()
    
        k = 10
        width = int((picture.shape[1])/k)
        height = int((picture.shape[0])/k)
        
        picture = cv2.resize(picture, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imwrite("compressed.jpg", picture)
        
        with open("compressed.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        ser.write(encoded_string)
        time.sleep(0.1)
        
        
        command = ser.readline().decode()

        if command != "":    
            if command == "forward":
                print("forward")
                motor_control.forward()
                
            elif command == "backward":
                print("backward")
                motor_control.backward()
                
            elif command == "left":
                print("left")
                motor_control.turn_left()
                
            elif command == "right":
                print("right")
                motor_control.turn_right()
            else:
                print(command)
                
    except:
        connect()
    



            

        
            

