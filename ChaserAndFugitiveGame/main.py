#main.py

import time
import sys
import world
import event
import error
import os

world.World.chaserList.append(world.Chaser())
gamer = world.World.chaserList[0]
lastMessage = ""

while True:
    os.system('cls')
    
    print("Time Enlapsed: {0}\n".format(world.World.time))
    
    if world.World.time % 5 == 0:
        message = event.Event.printNewCharacter("Fugitive", world.World.addFugitive())
        lastMessage = message
        print(lastMessage + " <<< ")
    else:
        print(lastMessage)

    print("")
    
    message = event.Event.printIfFugitiveCatched()
    if message: 
        print("\n\n{}\n\n".format(message))
        exit()    

    print('- ' * 12)
    
    for i in range(21):
        print("|", end = '')
        for m in world.World.map[i]:
            print(m, end = '')
        print("|")
        
    print('- ' * 12)
    print("\n\n")
    
    time.sleep(0.5)
    world.World.time = world.World.time + 1

    gamer.pastY = gamer.y
    gamer.pastX = gamer.x
    world.World.map[gamer.y][gamer.x] = ' '
    gamer.move()
    error.OutOfMapError.check(gamer)
    error.TooFastMoveError.check(gamer)
    world.World.map[gamer.y][gamer.x] = 'C'

    
    for f in world.World.fugitiveList:
        f.move()
        error.OutOfMapError.check(f)
        error.TooFastMoveError.check(f)