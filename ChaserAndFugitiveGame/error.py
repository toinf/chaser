#error.py
import sys
import re
import world

class Error(Exception):
    valueX = 0 #the position where a error occured
    valueY = 0
    message = "basic error class"

class OutOfMapError(Error):
    message = "OutOfMapError"
    def check(character):
        if(character.x > 20 or character.x < 0 or character.y > 20 or character.y < 0):
            print(OutOfMapError.message + ": " + character.name + str(character.number) + ", x: " + str(character.x) + ", y: " + str(character.y))
            sys.exit()
    def __init__(self, valueY, valueX):
        self.valueY = valueY
        self.valueX = valueX

class TooFastMoveError(Error):
    message = "TooFastMoveError"
    def check(character):
        if((abs(character.x - character.pastX) + abs(character.y - character.pastY)) > 1):
            print(TooFastMoveError.message + ": " + character.name + str(character.number) + ", x: " + str(character.x) + ", y: " + str(character.y))
            sys.exit()
    def __init__(self, valueY, valueX):
        self.valueY = valueY
        self.valueX = valueX

class CharacterOverlapedError(Error):
    message = "CharacterOverlapedError"
    def check(character):
        if(character.name == "Fugitive"):
            for f in world.fugitiveList:
                if((f.number != character.number) and (f.x == character.x) and (f.y == character.y)):
                    print(CharacterOverlapedError.message + ": " + character.name + str(character.number) + ", x: " + str(character.x) + ", y: " + str(character.y))
                    sys.exit()
    def __init__(self, valueY, valueX):
        self.valueY = valueY
        self.valueX = valueX
