import pygame
from pygame.locals import *
from particle import Particle
from forces import Gravity

SCREENSIZE = (600,400)
pygame.init()
screen 

p = Particle(40, 100)
gravity = Gravity()

while True:
    gravity.updateForce(particle)
    particle.update(dt)
    particle.render(screen)
