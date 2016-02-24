from vectors import Vector2D

class Entity(object):
    def __init__(self):
        self.ID = 0
        self.position = Vector2D()
        self.velocity = Vector2D()
        self.acceleration = Vector2D()
        self.Fnet = Vector2D()
        self.mass = 0
        self.invMass = 0
        
    def update(self, dt):
        pass
    
    def setMass(self, mass):
        self.mass = mass
        if mass > 0:
            self.invMass = 1.0 / mass
    
    def addForce(self, force):
        self.Fnet += force
        
    def render(self, screen):
        vals = list(self.position.toTuple()) + [2,2]
        pygame.draw.rect(screen, (200,0,0), vals)
    
