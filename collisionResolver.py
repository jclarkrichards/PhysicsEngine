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
        '''separting axis theorem for rectangles.  
        Need to include circles as well in the future'''
        if self.xAxisGap(self.entity1.position, self.entity2.position):
            return False
        if self.yAxisGap(self.entity1.position, self.entity2.position):
            return False
        return True
#------------------------------------------------------------------------------        
    def xAxisGap(self, pos1, pos2):
        '''Returns True if there is a gap'''
        check1 = (pos1.x + self.entity1.w) <= pos2.x
        check2 = pos1.x >= (pos2.x + self.entity2.w)
        return check1 or check2
        
    def yAxisGap(self, pos1, pos2):
        check1 = (pos1.y + self.entity1.h) <= pos2.y
        check2 = pos1.y >= (pos2.y + self.entity2.h)
        return check1 or check2
    
    def resolveVelocity(self, dt):
        pass
    
    def resolveCollision(self, dt):
        '''Separate objects so no longer penetrating.  
        Depends on objects shape.  Assume rectangles for now.  
        Also assumes entity2 is static.'''
        #Right before collision there was at least one separating axis
        #Get the previous position of entity1 and entity2
        #for stationary objects pp2 == entity2.position
        pp1 = self.entity1.position - self.entity1.velocity*dt
        pp2 = self.entity2.position - self.entity2.velocity*dt
        #xgap1, xgap2, ygap1, ygap2 = (0,0,0,0)
        #print "YGAP"
        #if pp2.y > (pp1.y+self.entity1.h):
        #    print pp2.y - (pp1.y+self.entity1.h)
        #if pp1.y > (pp2.y+self.entity2.h):
        #    print pp1.y - (pp2.y+self.entity2.h)
            
        #print "XGAP"
        #if pp2.x > (pp1.x+self.entity1.w):
        #    print pp2.x - (pp1.x+self.entity1.w)
        #if pp1.x > (pp2.x+self.entity2.w):
        #    print pp1.x - (pp2.x+self.entity2.w)
            

        #print ''

        #if y is the separating axis
        if self.yAxisGap(pp1, pp2):
            #Entity1 above entity2
            if pp2.y > (pp1.y+self.entity1.h):
                gap = pp2.y - (pp1.y + self.entity1.h)
                #if entity1 y was stationary during collision
                if pp1.y == self.entity1.position.y:
                    self.entity2.position.y = pp2.y - gap
                    self.entity2.velocity.y = 0.0
                if pp2.y == self.entity2.position.y:
                    self.entity1.position.y = pp1.y + gap
                    self.entity1.velocity.y = 0.0
                if (pp1.y != self.entity1.position.y and
                    pp2.y != self.entity2.position.y):
                    self.entity1.position.y = pp1.y + gap/2.0 - 1
                    self.entity2.position.y = pp2.y - gap/2.0
                    
                    self.entity1.velocity.y = 0.0
                    self.entity2.velocity.y = 0.0
            #Entity1 below entity2
            if pp1.y > (pp2.y+self.entity2.h):
                gap = pp1.y - (pp2.y+self.entity2.h)
                #if entity1 y was stationary before collision
                if pp1.y == self.entity1.position.y:
                    self.entity2.position.y = pp2.y + gap
                    self.entity2.velocity.y = 0.0
                if pp2.y == self.entity2.position.y:
                    self.entity1.position.y = pp1.y - gap
                    self.entity1.velocity.y = 0.0
                if (pp1.y != self.entity1.position.y and
                    pp2.y != self.entity2.position.y):
                    self.entity1.position.y = pp1.y - gap/2.0
                    self.entity2.position.y = pp2.y + gap/2.0 - 1
                    
                    self.entity1.velocity.y = 0.0
                    self.entity2.velocity.y = 0.0
        
        elif self.xAxisGap(pp1, pp2): #assume x was the separating axis
            #Entity1 to the left of entity2
            print "TO THE LEFT"
            if pp2.x > (pp1.x+self.entity1.w):
                gap = pp2.x - (pp1.x + self.entity1.w)
                #If entity1 x was stationary before collision
                if pp1.x == self.entity1.position.x:
                    self.entity2.position.x = pp2.x - gap
                    self.entity2.velocity.x *= -1
                if pp2.x == self.entity2.position.x:
                    self.entity1.position.x = pp1.x + gap
                    self.entity1.velocity.x *= -1
                if (pp1.x != self.entity1.position.x and
                    pp2.x != self.entity2.position.x):
                    self.entity1.position.x = pp1.x + gap/2.0
                    self.entity2.position.x = pp2.x - gap/2.0
                    
                    if (self.entity1.velocity.x > 0 and
                        self.entity2.velocity.x < 0):
                        self.entity1.velocity.x *= -1
                        self.entity2.velocity.x *= -1
                    elif (self.entity1.velocity.x < 0 and
                          self.entity2.velocity.x < 0):
                        if (self.entity1.velocity.x >
                            self.entity2.velocity.x):
                            self.entity2.velocity.x *= -1
                    elif (self.entity1.velocity.x > 0 and
                          self.entity2.velocity.x > 0):
                        if (self.entity1.velocity.x >
                            self.entity2.velocity.x):
                            self.entity1.velocity.x *= -1
                    
                    #self.entity1.velocity.x *= -1
                    #self.entity2.velocity.x *= -1
            #Entity1 to the right of entity2
            if pp1.x > (pp2.x+self.entity2.w):
                gap = pp1.x - (pp2.x+self.entity2.w)
                #If entity2 was stationary before collision
                if pp1.x == self.entity1.position.x:
                    self.entity2.position.x = pp2.x + gap
                    self.entity2.velocity.x *= -1
                if pp2.x == self.entity2.position.x:
                    self.entity1.position.x = pp1.x - gap
                    self.entity1.velocity.x *= -1
                if (pp1.x != self.entity1.position.x and
                    pp2.x != self.entity2.position.x):
                    self.entity1.position.x = pp1.x - gap/2.0
                    self.entity2.position.x = pp2.x + gap/2.0
                    
                    if (self.entity1.velocity.x < 0 and
                        self.entity2.velocity.x > 0):
                        self.entity1.velocity.x *= -1
                        self.entity2.velocity.x *= -1
                    elif (self.entity1.velocity.x < 0 and
                          self.entity2.velocity.x < 0):
                        if (self.entity2.velocity.x >
                            self.entity1.velocity.x):
                            self.entity1.velocity.x *= -1
                    elif (self.entity1.velocity.x > 0 and
                          self.entity2.velocity.x > 0):
                        if (self.entity2.velocity.x >
                            self.entity1.velocity.x):
                            self.entity2.velocity.x *= -1

                        
                    #self.entity1.velocity.x *= -1
                    #self.entity2.velocity.x *= -1
            #self.entity1.velocity.x *= -1  #move in opposite direction
            
    

    
    def calculateSeparatingVelocity(self):
        pass
