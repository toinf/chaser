#main.py

import time
import sys
import world
import event
import error

world.World.chaserList.append(world.Chaser())
gamer = world.World.chaserList[0]
lastMessage = ""

while True:
    print("time: {0}".format(world.World.time))
    if world.World.time % 5 == 0:
        world.World.fugitiveList.append(world.Fugitive())
    else:
        print()
    message = event.Event.printIfFugitiveCatched()
    if message: 
        lastMessage = message
    event.Event.printIfAllFugitiveCatched()
    print(lastMessage) 

    print('- ' * 12)
    for i in range(0, 20):
        print("|", end = '')
        for m in world.World.map[i]:
            print(m, end = '')
        print("|")
        
    print('- ' * 12)
    print()
    print('- ' * 12)
    
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