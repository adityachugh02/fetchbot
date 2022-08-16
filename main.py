import cv2
from flask import Flask, flash, request, send_from_directory, render_template, Response
import serial
import time
import numpy as np
import base64
from PIL import Image
from flask_cors import CORS, cross_origin
import subprocess


image = 200*np.ones((80,100,3), dtype=np.uint8)
ret, jpeg = cv2.imencode('.jpg', image)
pic = jpeg.tobytes()

ser = None
message = ""

def connect():

    global ser

    while True:
        if ser == None:
            try:
                ser = serial.Serial("COM7", timeout=0, baudrate=115000)
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
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/index')
def index():
    global message
    connect()
    return render_template("index.html")

@app.route('/jquery-3.6.0.js')
def js():
    return app.send_static_file('jquery-3.6.0.js')

@app.route('/video_feed')
def video_feed():
    return Response(display_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/command', methods=['POST'])
def command():
    command = ((request.data).decode())
    try:
        ser.write(command.encode())
    except:
        connect()
    return "200"

@app.route('/code', methods=['POST'])
def code():
    global proc

    code = ((request.data).decode())
    if code != "":
        code_head ='''
import src.fetchbot as fetchbot
import time

'''

        code = code_head + code
        with open("temp.py", "w+") as file:
            file.write(code)

        try:
            subprocess.Popen.terminate(proc)
        except:
            print("No process to terminate")

        proc = subprocess.Popen(['python','temp.py'])

    else:
        try:
            subprocess.Popen.terminate(proc)
        except:
            print("No process to terminate")
        global message
        message = ""

    return "200"

@app.route('/message_in', methods=['POST'])
def message_in():
    global message
    message = ((request.data).decode())
    return "200"

@app.route('/message_out', methods=['POST'])
def message_out():
    return Response(message)




app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)