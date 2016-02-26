from vectors import Vector2D

class EntityCollisionResolver(object):
    def __init__(self):
        self.entities = [None, None]
        #self.restitution = 0
        #self.contactNormal = Vector2D()
        #self.penetration = 0
        #self.penetrateX, self.penetrateY = (0,0)
    
    def setEntityPair(self, entity1, entity2):
        self.entities[0] = entity1
        self.entities[1] = entity2
        
    def resolve(self, dt):
        colliding = self.calculateCollision()
        if colliding:
            self.resolveCollision(dt)
    
    def calculateCollision(self):
        '''Determine which collision detection to use here.  Assume rect to rect for now.'''
        colliding = self.calculateSeparatingAxes()
        return colliding
    
    def calculateSepartingAxes(self):
        '''separting axis theorem for rectangles.  Need to include circles as well in the future'''
        xOverlap, yOverlap = (False, False)
        xValues = (self.entities[0].position.x, self.entities[1].position.x, self.entities[0].w, self.entities[1].w]
        xOverlap = self.axisOverlap(*xValues)
        if xOverlap:
            yValues = (self.entities[0].position.y, self.entities[1].position.y, self.entities[0].h, self.entities[1].h]
            yOverlap = self.axisOverlap(*yValues)
        return xOverlap & yOverlap
        
    def axisOverlap(self, p1, p2, l1, l2):
        '''check for axis overlap giving positions and lengths'''
        if p1 < p2:
            if p2+l2-p1 < l1+l2:
                return True
        elif p1 > p2:
            if p1+l1-p2 < l1+l2:
                return True
        elif p1 == p2:
            if l1 < l2:
                return True
            elif l1 > l2:
                return True
            return True
        return False
    
    def resolveVelocity(self, dt):
        pass
    
    def resolveCollision(self, dt):
        '''Separate objects so no longer penetrating.  Depends on objects shape.  Assume rectangles for now.  
        Also assumes entities[1] is static.'''
        #Right before collision there was at least one separating axis
        previousPosition = self.entities[0].position - self.entities[0].velocity*dt
        xValues = (previousPosition.x, self.entities[1].position.x, self.entities[0].w, self.entities[1].w]
        xOverlap, dx = self.axisOverlap(*xValues)
        #if xoverlap, assume y is the separating axis
        if xOverlap:
            if self.entities[0].position.y < self.entities[1].position.y:
                self.entities[0].position.y = self.entities[1].position.y - self.entities[0].height
            elif self.entities[0].position.y > self.entities[1].position.y:
                self.entities[0].position.y = self.entities[1].position.y + self.entities[1].height
        else: #assume x was the separating axis
            if self.entities[0].position.x < self.entities[1].position.x:
                self.entities[0].position.x = self.entities[1].position.x - self.entities[0].width
            elif self.entities[0].position.x > self.entities[1].position.x:
                self.entities[0].position.x = self.entities[1].position.x + self.entities[1].width
        
    
    
    def calculateSeparatingVelocity(self):
        pass
