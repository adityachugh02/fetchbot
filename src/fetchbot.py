import requests
import os

def move(direction):
    try:
        requests.post('http://localhost:5000/command', data = direction, timeout=0.0000001)
    except:
        pass
    return

def say(message):
    try:
        requests.post('http://localhost:5000/message_in', data = message, timeout=0.0000001)
    except:
        pass
    return