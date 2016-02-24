from vectors import Vector2D

class Entity(object):
    def __init__(self):
        self.ID = 0
        self.position = Vector2D()
        self.velocity = Vector2D()
        self.acceleration = Vector2D()
        
    def update(self, dt):
        pass
    
    def render(self, screen):
        vals = list(self.position.toTuple()) + [2,2]
        pygame.draw.rect(screen, (200,0,0), vals)
    
