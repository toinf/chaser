#world.py

import random
import sys
import event
import error

class World:
    time = 0
    fugitiveList = []
    chaserList = []
    map = [[' '] * 21,
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21,
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21, 
           [' '] * 21]
    def _init_(self):
        pass

class Character:
    x = 0
    y = 0
    pastX = 0
    pastY = 0
    shape = 'N'
    count = 0
    number = 0
    name = "none"
    def __init__(self): #not actually use!
        while True:
            self.x = random.randint(0, 20)
            self.y = random.randint(0, 20)
            if World.map[self.y][self.x] == ' ':
                self.pastX = self.x
                self.pastY = self.y
                break
    def __del__(self):
        Character.count = Character.count - 1
    def move(self):
        print("Wrong move: character not declared")

class Fugitive(Character):
    shape = 'F'
    name = "Fugitive"
    def __init__(self):
        super().__init__()
        self.number = Fugitive.count
        Fugitive.count = Fugitive.count + 1
        World.map[self.y][self.x] = Fugitive.shape
        event.Event.printNewCharacter("Fugitive", self.number)
    def __del__(self):
        super().__del__()

    def move(self):
        while True:
            tempX = random.randint(-1, 1)
            if tempX == 0:
                tempY = random.randint(-1, 1)
            else:
                tempY = 0
            if (self.x + tempX) > -1 and (self.x + tempX) < 21:
                if (self.y + tempY) > -1 and (self.y + tempY) < 21:
                    if World.map[self.y + tempY][self.x + tempX] == ' ':
                        self.pastY = self.y
                        self.pastX = self.x
                        World.map[self.y][self.x] = ' '
                        self.y = self.y + tempY
                        self.x = self.x + tempX
                        World.map[self.y][self.x] = Fugitive.shape
                        break
    """def move(self):
        self.pastY = self.y
        self.pastX = self.x
        World.map[self.y][self.x] = ' '
        if abs(World.chaserList[0].y - self.y) + abs(World.chaserList[0].x - self.x) > 5:
            while True:
                tempX = random.randint(-1, 1)
                if tempX == 0:
                    tempY = random.randint(-1, 1)
                else:
                    tempY = 0
                if (self.x + tempX) > -1 and (self.x + tempX) < 21:
                    if (self.y + tempY) > -1 and (self.y + tempY) < 21:
                        if World.map[self.y + tempY][self.x + tempX] == ' ':
                            self.y = self.y + tempY
                            self.x = self.x + tempX
                            break
        else:
            if World.chaserList[0].y > self.y and self.y != 0:
                self.y = self.y - 1
            elif World.chaserList[0].y < self.y and self.y != 20:
                self.y = self.y + 1
            elif World.chaserList[0].x > self.x and self.x != 0:
                self.x = self.x - 1
            elif World.chaserList[0].x < self.x and self.x != 20:
                self.x = self.x + 1
        World.map[self.y][self.x] = Fugitive.shape"""

class Chaser(Character):
    shape = 'C'
    name = "Chaser"
    def __init__(self):
        super().__init__()
        Chaser.x = self.x
        Chaser.y = self.y
        Chaser.number = Chaser.count
        Chaser.count = Chaser.count + 1
        World.map[Chaser.y][Chaser.x] = Chaser.shape
        event.Event.printNewCharacter("Chaser", Chaser.number)
    def __del__(self):
        super()
    def move(self):
        #Your code hear!!
        #
        #
        self.x = self.x + 1