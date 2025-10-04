import random

def get_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'c.join':
    return 'You have joined the game!'

  if message == 'c.roll':
    r = random.randint(1,6)
    falien = [1, 2, 3]
    fx = [4, 5]
    fs = [6]
    if r in falien:
      return "Alien"
    elif r in fx:
      return "X"
    elif r in fs:
      return "Syringe"

  if message == 'help':
    return 'help message'

  return 'Unknown Command'
