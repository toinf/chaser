#event.py
import world

class Event:
    pastFugitiveCount = 0
    def printNewCharacter(name, number):
        print("time: " + str(world.World.time) + ", " + name + str(number) + " occured.")
    def printIfFugitiveCatched():
        for f in world.World.fugitiveList:
            if world.Chaser.x == f.x and world.Chaser.y == f.y:
                print("time: " + str(world.World.time) + ", " + f.name + str(f.number) + " catched.")
                world.World.fugitiveList.pop(f)
    def printIfAllFugitiveCatched():
        if world.Fugitive.count == 0 and Event.pastFugitiveCount != 0:
            print("time: " + str(world.World.time) + ", cleard")
        Event.pastFugitiveCount = world.Fugitive.count