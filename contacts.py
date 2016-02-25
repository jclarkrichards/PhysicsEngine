from vectors import Vector2D

class EntityContacts(object):
    def __init__(self):
        self.entities = [None, None]
        self.restitution = 0
        self.contactNormal = Vector2D()
        self.penetration = 0
    
    def getEntityPair(self, entity1, entity2):
        self.entities[0] = entity1
        self.entities[1] = entity2
        
    def resolve(self, dt):
        pass
    
    def calculateSeparatingVelocity(self):
        pass
    
    def resolveVelocity(self, dt):
        pass
    
    def resolvePenetration(self, dt):
        pass
