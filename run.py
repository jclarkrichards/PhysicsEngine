import pygame
from pygame.locals import *
from particle import Particle
#from forces import Gravity
from forceRegistry import ForceRegistry
from world import World
from entity import Entity

SCREENSIZE = (600,400)
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.surface.Surface(SCREENSIZE).convert()
background.fill((0,0,0))
clock = pygame.time.Clock()

particle = Entity(40, 100)
particle.setSize(16,16)
particle.setMass(20)
particle.setVelocity(60,-100)

particle2 = Entity(440, 100)
particle2.setSize(32,32)
particle2.setMass(40)
particle2.setVelocity(-40,-100)

#Set a static floor object
floor = Entity(0,250)
floor.setSize(350, 60)
floor2 = Entity(550,200)
floor2.setSize(30,50)
floor3 = Entity(70,40)
floor3.setSize(50,20)
floor4 = Entity(100, 100)
floor4.setSize(40,10)
floor5 = Entity(0,200)
floor5.setSize(20,60)
floor6 = Entity(352,250)
floor6.setSize(200,60)
world = World()
world.addDynamicObject(particle)
world.addDynamicObject(particle2)
world.addStaticObject(floor)
world.addStaticObject(floor2)
world.addStaticObject(floor3)
world.addStaticObject(floor4)
world.addStaticObject(floor5)
world.addStaticObject(floor6)

#gravity = Gravity()
registry = ForceRegistry()
registry.addGravity(particle)
registry.addGravity(particle2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    dt = clock.tick(30) / 1000.0
    registry.updateForces(dt)
    #gravity.updateForce(particle)
    #particle.update(dt)
    #particle2.update(dt)
    world.integrateObjects(dt)
    screen.blit(background, (0,0))
    #particle.render(screen)
    #particle2.render(screen)
    world.render(screen)
    #print particle.position
    pygame.display.update()
