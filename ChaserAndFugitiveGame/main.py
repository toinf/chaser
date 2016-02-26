#main.py

import time
import sys
import world
import event
import error
import os

world.World.chaserList.append(world.Chaser())
gamer = world.World.chaserList[0]
newMessage = ""

while True:
    os.system('cls')
    
    print("Time Enlapsed: {0}\n".format(world.World.time))
    
    lastMessage = newMessage
    
    if world.World.time % 10 == 0:
        newMessage = event.Event.printNewCharacter("Fugitive", world.World.addFugitive())
    message = event.Event.printIfFugitiveCatched()
    if message:
        newMessage = message
    
    if newMessage != lastMessage:
        print(newMessage + " <<< ")
    else:
        print(newMessage)

    print("")
    
    message = event.Event.printIfAllFugitiveCatched()
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
    
    time.sleep(0.2)
    world.World.time = world.World.time + 1

    gamer.pastY = gamer.y
    gamer.pastX = gamer.x
    world.World.map[gamer.y][gamer.x] = ' '
    try:
        gamer.move()
    except error.OutOfMapError as e:
        print("\n\nERROR: [ cannot access out of map range ]")
        print("Error coordinate: ({0}, {1})".format(e.valueX, e.valueY))
        exit()
    world.Chaser.x = gamer.x
    world.Chaser.y = gamer.y
    error.OutOfMapError.check(gamer)
    error.TooFastMoveError.check(gamer)
    world.World.map[gamer.y][gamer.x] = 'C'

    
    for f in world.World.fugitiveList:
        f.move()
        error.OutOfMapError.check(f)
        error.TooFastMoveError.check(f)