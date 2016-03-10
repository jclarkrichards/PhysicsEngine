import pygame
from forceRegistry import ForceRegistry
from world import World
from entity import Entity

world = World()
world.setup(600, 400)

clock = pygame.time.Clock()

particle = Entity(40, 100)
particle.setSize(16,16)
particle.setMass(20)
particle.setVelocity(80,-100)
#particle.isImpenetrable = False

particle2 = Entity(440, 100)
particle2.setSize(32,32)
particle2.setMass(40)
particle2.setVelocity(-40,-100)
#particle2.isImpenetrable = False

#Set a static floor object
floor = Entity(0,250)
floor.setSize(350, 60)
floor2 = Entity(550,200)
floor2.setSize(30,50)
floor3 = Entity(70,40)
floor3.setSize(50,20)
floor4 = Entity(100, 100)
floor4.setSize(100,10)
floor5 = Entity(0,200)
floor5.setSize(20,60)
floor6 = Entity(360,250)
floor6.setSize(200,60)
floor7 = Entity(240,0)
floor7.setSize(20, 200)

other1 = Entity(334, 210)
other1.setSize(radius=40)
other2 = Entity(23, 20)
other2.setSize(radius=15)

world.addDynamicObject(particle)
#world.addDynamicObject(particle2)
world.addStaticObject(floor)
world.addStaticObject(floor2)
world.addStaticObject(floor3)
world.addStaticObject(floor4)
world.addStaticObject(floor5)
world.addStaticObject(floor6)
world.addStaticObject(floor7)
world.addOtherObject(other1)
world.addOtherObject(other2)

#Get master list of all possible collision pairs
#world.setContactingPairs()

registry = ForceRegistry()
registry.addGravity(particle)
#registry.addGravity(particle2)

while True:
    world.handleEvents()
    dt = clock.tick(30) / 1000.0
    registry.updateForces(dt)
    world.integrateObjects(dt)
    world.render()
    world.cleanUp()
    pygame.display.update()
