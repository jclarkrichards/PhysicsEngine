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

particle = Particle(40, 100)
particle.setMass(20)
particle.setVelocity(40,-100)

particle2 = Particle(440, 100)
particle2.setMass(40)
particle2.setVelocity(-40,-100)

#Set a static floor object
floor = Entity(0,380)
floor.setSize(600, 30)

world = World()
world.addDynamicObject(particle)
world.addDynamicObject(particle2)
world.addStaticObject(floor)

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
    pygame.display.update()
