import pygame
from vectors import Vector2D

class Entity(object):
    def __init__(self, x, y):
        self.ID = None
        self.position = Vector2D(x, y)
        self.velocity = Vector2D()
        self.acceleration = Vector2D()
        self.Fnet = Vector2D()
        self.mass = 0
        self.invMass = 0
        self.w, self.h = (0, 0)
        
    def update(self, dt):
        self.position += self.velocity*dt
        self.acceleration = self.Fnet #*self.invMass
        self.velocity += self.acceleration*dt
        self.Fnet = Vector2D()
    
    def setSize(self, width, height):
        self.w = width
        self.h = height
        
    def setID(self, identification):
        self.ID = identification
        
    def setMass(self, mass):
        self.mass = mass
        if mass > 0:
            self.invMass = 1.0 / mass

    def setVelocity(self, vx, vy):
        self.velocity = Vector2D(vx, vy)
        
    def addForce(self, force):
        self.Fnet += force
        
    def render(self, screen):
        vals = list(self.position.toTuple()) + [self.w, self.h]
        pygame.draw.rect(screen, (200,0,0), vals)
    
