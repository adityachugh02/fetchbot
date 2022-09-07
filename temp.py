
# coding: latin-1
import src.fetchbot as fetchbot
import time

while True:
  fetchbot.move("forward")
  time.sleep(1)
  fetchbot.move("backward")
  time.sleep(1)
