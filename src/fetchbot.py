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
        requests.post('http://localhost:5000/message_in', data = str(message), timeout=0.1)
    except:
        pass
    return

def predict():
    try:
        response = requests.post('http://localhost:5000/predict', data = "class", timeout=0.5)
        return response.text
    except:
        pass

def score():
    try:
        response = requests.post('http://localhost:5000/predict', data = "score", timeout=0.5)
        return int(response.text)
    except:
        pass