#event.py

import world

class Event:
    pastFugitiveCount = 0
    def printNewCharacter(name, number):
        return "{0} {1} occured at time {2}".format(name, number, world.World.time)
        
    def printIfFugitiveCatched():
        for i in range(len(world.World.fugitiveList)):
            l = world.World.fugitiveList
            f = l[i]
            if world.Chaser.x == f.x and world.Chaser.y == f.y:
                message = "{0}{1} catched at time {2}".format(f.name, f.number, world.World.time)
                del world.World.fugitiveList[i]
                world.World.map[world.Chaser.y][world.Chaser.x] = 'C'
                return message
                
    def printIfAllFugitiveCatched():
        if world.Fugitive.count == 0 and Event.pastFugitiveCount != 0:
            return "All fugitives are cleared at time {}".format(world.World.time)
        Event.pastFugitiveCount = world.Fugitive.count
        