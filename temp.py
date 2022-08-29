
# coding: latin-1
import src.fetchbot as fetchbot
import time

_C3_A9l_C3_A9ment = None


while True:
  _C3_A9l_C3_A9ment = ''
  if (fetchbot.predict()) == 'rien':
    fetchbot.move("forward")
  if (fetchbot.predict()) == 'line':
    fetchbot.say(fetchbot.predict())
    fetchbot.move("backward")
    fetchbot.move("left")
  _C3_A9l_C3_A9ment = str(_C3_A9l_C3_A9ment) + str(fetchbot.predict())
  _C3_A9l_C3_A9ment = str(_C3_A9l_C3_A9ment) + ': '
  _C3_A9l_C3_A9ment = str(_C3_A9l_C3_A9ment) + str(fetchbot.score())
  fetchbot.say(_C3_A9l_C3_A9ment)
