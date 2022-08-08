import cv2
from flask import Flask, flash, request, send_from_directory, render_template, Response
import serial
import time
import numpy as np
import base64
from PIL import Image


image = 200*np.ones((80,100,3), dtype=np.uint8)
ret, jpeg = cv2.imencode('.jpg', image)
pic = jpeg.tobytes()

ser = None
delay = time.time()

def connect():

    global ser

    while True:
        if ser == None:
            try:
                ser = serial.Serial("COM8", timeout=0, baudrate=115000)
                print("Connected")
                return
            except:
                print("No connection")
                time.sleep(1)
        else:
            try:
                ser.close()
                ser = None
                print("disconnecting, reconnecting...")
                time.sleep(1)
            except:
                print("error")
                time.sleep(1)


def display_video():

    global pic
    global time

    while True:
        try:
            image = ser.readline().decode()
        except:
            time.sleep(1)
            image = ""

        if image !="":
            try: 
                image_2 = base64.b64decode(str(image))
                nparr = np.frombuffer(image_2, np.uint8)
                image_2 = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED) 
                ret, jpeg = cv2.imencode('.jpg', image_2)
                pic = jpeg.tobytes()
            except:
                pass
            #print("Video stream error")

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + pic + b'\r\n\r\n')
 

app = Flask(__name__)

@app.route('/video')
def video():
    connect()
    return render_template("video.html")

@app.route('/video_feed')
def video_feed():
    return Response(display_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/command', methods=['POST'])
def command():
    print(request.form)
    return "valid"

@app.route('/code', methods=['POST'])
def code():
    print(request.form)
    return "valid"



app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)