from vectors import Vector2D

class Force(object):
    def __init__(self):
        pass
    
    def updateForce(self, entity, dt=0):
        pass
    

class Gravity(Force):
    def __init__(self):
        Force.__init__(self)
        self.gravity = Vector2D(0, 100)
    
    def updateForce(self, entity, dt=0):
        #if entity.invMass != 0:
        entity.addForce(self.gravity) #*entity.mass)


class Drag(Force):
    def __init__(self):
        Force.__init__(self)
