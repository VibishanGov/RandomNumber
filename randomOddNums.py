#!/usr/bin/python

import random

def generateNumber():
  number = random.randint(0, 99)
  if number % 2 == 0:
    number = number + 1
  
  return number

if __name__ == "__main__":
  print(generateNumber())