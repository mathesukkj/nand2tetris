from random import randint
from time import sleep

keyboardAddr = 24576 - 16384
screenMemoryEnd = keyboardAddr
screenAddresses = [0 for x in range(screenMemoryEnd)]

def main():
  while True:
    loop()
    sleep(1)

def loop():
  keyboardValue = randint(0, 1) # here is supposed to be the kbd address
  if keyboardValue != 0:
    black()
  else:
    white()

def black():
  for i in range(screenMemoryEnd):
    screenAddresses[i] = 1


def white():
  for i in range(screenMemoryEnd):
    screenAddresses[i] = 0

main()