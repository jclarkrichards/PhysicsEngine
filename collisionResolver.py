"""An entity pair is defined as entity1 and entity2.  """
from vectors import Vector2D

class EntityCollisionResolver(object):
    def __init__(self):
        self.entity1, self.entity2 = (None, None)
        self.xOverlap, self.yOverlap = (0.0, 0.0)
        self.pairs = []
        
        #self.restitution = 0
        #self.contactNormal = Vector2D()
        #self.penetration = 0
        #self.penetrateX, self.penetrateY = (0,0)
    
    def addPair(self, pair):
        '''Add an entity pair'''
        self.pairs.append(pair)
        
    def clearPairs(self):
        self.pairs = []
        
    def setEntityPair(self, entity1, entity2):
        '''Set the entity pair to be used for collision resolution'''
        self.entity1, self.entity2 = (entity1, entity2)
        
    def setOverlaps(self, x, y):
        '''Set the overlaps of entities if found previously'''
        self.xOverlap = x
        self.yOverlap = y
     
    def resolve(self, dt):
        pairDict = {}
        for pair in self.pairs:
            self.setEntityPair(*pair)
            colliding = self.calculateCollision()
            if colliding:
                pairDict[pair] = self.getOverlapArea()
        pairSorted = sorted(pairDict.items(), key=lambda x: x[1], reverse=True)
        self.pairs = [k[0] for k in pairSorted]
        #print len(self.pairs)
        for pair in self.pairs:
            self.setEntityPair(*pair)
            self.resolveCollision(dt)
        self.clearPairs()
    
    def calculateCollision(self):
        '''Determine which collision detection to use here.  Assume rect to rect for now.'''
        if self.entity1.radius and self.entity2.radius:
            colliding = self.calculateCircleCircleOverlap()
        elif self.entity1.radius and not self.entity2.radius:
            colliding = self.calculateCircleAABBOverlap()
        elif not self.entity1.radius and self.entity2.radius:
            colliding = self.calculateCircleAABBOverlap()
        else:
            #rect and rect collision
            colliding = self.calculateSeparatingAxes()
        return colliding
    
    def calculateSeparatingAxes(self):
        '''separting axis theorem for rectangles.  
        Need to include circles as well in the future'''
        if self.xAxisGap(self.entity1, self.entity2):
            return False
        if self.yAxisGap(self.entity1, self.entity2):
            return False
        return True
        
    def calculateCircleCircleOverlap(self):
        pass
    
    def calculateCircleAABBOverlap(self):
        pass
#------------------------------------------------------------------------------        
    def xAxisGap(self, a, b):
        '''Returns True if there is a gap, False if overlap'''
        return b.min.x >= a.max.x or a.min.x >= b.max.x
        
    def yAxisGap(self, a, b):
        '''Returns True if there is a gap, False if overlap'''
        return b.min.y >= a.max.y or a.min.y >= b.max.y
        
    #Assuming there's an overlap detected already
    def getXOverlap(self, a, b):
        return min(a.max.x-b.min.x, b.max.x-a.min.x, a.max.x-a.min.x, b.max.x-b.min.x)
        
    def getYOverlap(self, a, b):
        return min(a.max.y-b.min.y, b.max.y-a.min.y, a.max.y-a.min.y, b.max.y-b.min.y)
    
    def resolveCollision(self, dt):
        '''Separate objects so no longer penetrating.  
        Depends on objects shape.  Assume rectangles for now.  
        Also assumes entity2 is static.'''
        #Right before collision there was at least one separating axis
        #Get the previous position of entity1 and entity2
        if self.entity1.radius and self.entity2.radius:
            #resolve circle circle collision
            self.resolveCircleCircle(self.entity1, self.entity2, dt)
        elif self.entity1.radius and not self.entity2.radius:
            #resolve circle and rect collision
            self.resolveCircleAABB(self.entity1, self.entity2, dt)
        elif not self.entity1.radius and self.entity2.radius:
            #resolve rect and circle collision
            self.resolveCircleAABB(self.entity2, self.entity1, dt)
        else:
            #resolve rect and rect collision
            self.resolveAABBAABB(self.entity1, self.entity2, dt)
            
    def resolveAABBAABB(self, a, b, dt):
        '''Resolve two rectangles colliding'''
        xOverlap = self.getXOverlap(a, b)
        yOverlap = self.getYOverlap(a, b)
        if 0 < yOverlap < xOverlap:
            if a.min.y > b.min.y:
                a.updatePosition(dy=yOverlap)
            else:
                a.updatePosition(dy=yOverlap*-1)
            #a.velocity.y = 0.0
            a.addImpulse(vx=a.velocity.x, vy=0.0)
        elif 0 < xOverlap < yOverlap:
            if a.min.x > b.min.x:
                a.updatePosition(dx=xOverlap)
            else:
                a.updatePosition(dx=xOverlap*-1)
            #a.velocity.x *= -1
            a.addImpulse(vx=a.velocity.x*-1, vy=a.velocity.y)
        elif xOverlap == yOverlap:
            pass
        
    def resolveCircleCircle(self, dt):
        pass
    
    def resolveCircleAABB(self, dt):
        pass
    
    def resolveAABBCircle(self, dt):
        pass
        '''
        pp1Min = self.entity1.min - self.entity1.velocity*dt
        pp2Min = self.entity2.min - self.entity2.velocity*dt
        pp1Max = pp1Min + self.entity1.size
        pp2Max = pp2Min + self.entity2.size
        vals = (pp1Min, pp1Max, pp2Min, pp2Max)
        xgap = self.getXAxisGap(*vals)
        ygap = self.getYAxisGap(*vals)
        
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
            '''
    

    
            
                
    def getOverlapArea(self):
        xOverlap = self.getXOverlap(self.entity1, self.entity2)
        yOverlap = self.getYOverlap(self.entity1, self.entity2)
        return xOverlap * yOverlap
        
        
            
    def calculateSeparatingVelocity(self):
        pass
