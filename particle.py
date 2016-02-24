from entity import Entity

class Particle(Entity):
    def __init__(self):
        Entity.__init__(self)
    
    def update(self, dt):
        self.position += self.velocity*dt
        self.acceleration = self.Fnet*self.invMass
        self.velocity += self.acceleration*dt
        self.Fnet = 0
    
    
  
