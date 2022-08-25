
# coding: latin-1
import src.fetchbot as fetchbot
import time

while True:
  if (fetchbot.predict()) == 'rien':
    fetchbot.say("Il n'y a rien...")
  if (fetchbot.predict()) == 'vert':
    fetchbot.say("Je vois un jeton vert!")
    fetchbot.move("forward")
  if (fetchbot.predict()) == 'rouge':
    fetchbot.say("Je vois un jeton rouge!")
    fetchbot.move("backward")
  if (fetchbot.predict()) == 'bleu':
    fetchbot.say("Je vois un jeton bleu!")
    fetchbot.move("right")
