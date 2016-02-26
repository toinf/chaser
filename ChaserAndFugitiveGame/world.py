#world.py

import random
import sys
import event
import error

def getList() {
    return world.World.fugitiveList
}

def getMap(x, y):
    if 0 <= x <= 20 and 0 <= y <= 20:
        return World.map[y][x]
    else:
        raise error.OutOfMapError(y, x)
class World:
    time = 0
    fugitiveList = []
    chaserList = []
    map = [[' ' for i in range(21)] for j in range(21)]
    
    def addFugitive():
        f = Fugitive()
        World.fugitiveList.append(f)
        return f.number
    
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
        raise Exception("Wrong move: character not declared")

class Fugitive(Character):
    shape = 'F'
    name = "Fugitive"
    def __init__(self):
        super().__init__()
        self.number = Fugitive.count
        Fugitive.count = Fugitive.count + 1
        World.map[self.y][self.x] = Fugitive.shape
        
    def __del__(self):
        super().__del__()
    
    def move(self):
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
                        
    def move2(self):
        self.pastY = self.y
        self.pastX = self.x
        World.map[self.y][self.x] = ' ' # Are you sure?
        chaser = World.chaserList[0]
        if abs(chaser.y - self.y) + abs(chaser.x - self.x) > 5:
            tempX = random.randint(-1, 1)
            if tempX == 0:
                tempY = random.randint(-1, 1)
            else:
                tempY = 0
            nx = self.x + tempX
            ny = self.y + tempY
            if 0 <= nx <= 20 and 0 <= ny <= 20 and World.map[ny][nx] == ' ':
                self.y = ny
                self.x = nx
        else:
            if chaser.y > self.y and self.y != 0:
                self.y = self.y - 1
            elif chaser.y < self.y and self.y != 20:
                self.y = self.y + 1
            elif chaser.x > self.x and self.x != 0:
                self.x = self.x - 1
            elif chaser.x < self.x and self.x != 20:
                self.x = self.x + 1
        World.map[self.y][self.x] = Fugitive.shape

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
        def inRange(x, y):
            return 0 <= x <= 20 and 0 <= y <= 20
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for i in range(4):
            nx = self.x + dx[i]
            ny = self.y + dy[i]
            if inRange(nx, ny):
                c = getMap(ny, nx)
                if c == 'C':
                    self.x = nx
                    self.y = ny
                    return
        
        if self.x % 2 == 1:
            if self.x != 20:
                self.x += 1
            elif self.x != 0:
                self.x -= 1
        else:
            if self.y != 20:
                self.y += 1
            elif self.y != 0:
                self.y -= 1
