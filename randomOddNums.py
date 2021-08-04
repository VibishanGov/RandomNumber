#!/usr/bin/python

import random

# function to generate a random odd number between 0 and 99
def generateNumber():
  number = random.randint(0, 99)
  if number % 2 == 0:
    number = number + 1
  
  return number

if __name__ == "__main__":
  print(generateNumber())