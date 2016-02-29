"""An entity pair is defined as entity1 and entity2.  """
from vectors import Vector2D

class EntityCollisionResolver(object):
    def __init__(self):
        self.entity1, self.entity2 = (None, None)
        #self.restitution = 0
        #self.contactNormal = Vector2D()
        #self.penetration = 0
        #self.penetrateX, self.penetrateY = (0,0)
    
    def setEntityPair(self, entity1, entity2):
        self.entity1, self.entity2 = (entity1, entity2)
     
    def resolve(self, dt):
        colliding = self.calculateCollision()
        if colliding:
            self.resolveCollision(dt)
    
    def calculateCollision(self):
        '''Determine which collision detection to use here.  Assume rect to rect for now.'''
        colliding = self.calculateSeparatingAxes()
        return colliding
    
    def calculateSeparatingAxes(self):
        '''separting axis theorem for rectangles.  Need to include circles as well in the future'''
        if xAxisGap(self.entity1.position, self.entity2.position):
            return False
        if yAxisGap(self.entity1.position, self.entity2.position):
            return False
        return True
#------------------------------------------------------------------------------        
    def xAxisGap(self, pos1, pos2):
        '''Returns True if there is a gap'''
        check1 = (pos1.x + self.entity1.w) < pos2.x
        check2 = pos1.x > (pos2.x + self.entity.w)
        return check1 or check2
        
    def yAxisGap(self, pos1, pos2):
        check1 = (pos1.y + self.entity1.h) < pos2.y
        check2 = pos1.y > (pos2.y + self.entity2.h)
        return check1 or check2
    
    def resolveVelocity(self, dt):
        pass
    
    def resolveCollision(self, dt):
        '''Separate objects so no longer penetrating.  
        Depends on objects shape.  Assume rectangles for now.  
        Also assumes entity2 is static.'''
        #Right before collision there was at least one separating axis
        #Get the previous position of entity1
        pp = self.entity1.position - self.entity1.velocity*dt
        
        #if y is the separating axis
        if yAxisGap(pp, self.entity2.position):
            #Entity1 above entity2
            if self.entity1.position.y < self.entity2.position.y:
                self.entity1.position.y = self.entity2.position.y - \
                                              self.entity1.h
                                            
            #Entity1 below entity2  
            elif self.entity1.position.y > self.entity2.position.y:
                self.entity1.position.y = self.entity2.position.y + \
                                              self.entity2.h
            self.entity1.velocity.y = 0.0
            
        else: #assume x was the separating axis
            if self.entity1.position.x < self.entity2.position.x:
                self.entity1.position.x = self.entity2.position.x - \
                                              self.entity1.w
            elif self.entity1.position.x > self.entity2.position.x:
                self.entity1.position.x = self.entity2.position.x + \
                                              self.entity2.w
            self.entity1.velocity.x *= -1
            
    

    
    def calculateSeparatingVelocity(self):
        pass
