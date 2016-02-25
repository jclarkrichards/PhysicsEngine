from entity import Entity
from vectors import Vector2D

class Particle(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
    
    def update(self, dt):
        self.position += self.velocity*dt
        self.acceleration = self.Fnet*self.invMass
        self.velocity += self.acceleration*dt
        self.Fnet = Vector2D()
    
    
  
