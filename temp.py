
import src.fetchbot as fetchbot
import time

while True:
  fetchbot.say("J'avance")
  fetchbot.move("forward")
  time.sleep(1)
  fetchbot.say("Je tourne a droite")
  fetchbot.move("right")
  time.sleep(1)
