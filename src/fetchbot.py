import requests

def fetchbot(direction):
    url = 'http://localhost:5000/command'
    x = requests.post(url, data = direction)
    return x
