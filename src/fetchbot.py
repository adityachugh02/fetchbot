import requests
import os

def move(direction):
    try:
        requests.post('http://localhost:5000/command', data = direction, timeout=0.1)
    except:
        pass
    return

def say(message):
    try:
        requests.post('http://localhost:5000/message_in', data = message, timeout=0.1)
    except:
        pass
    return

def predict():
    try:
        response = requests.post('http://localhost:5000/predict', timeout=0.1)
        return response.text
    except:
        pass