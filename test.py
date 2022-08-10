import requests

def fetchbot(direction):
    url = 'http://localhost:5000/message'
    x = requests.post(url, data = direction)
    return x

fetchbot("hello")