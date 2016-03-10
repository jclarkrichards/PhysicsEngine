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
    
    #Ultimately need to optimize the pairs before checking for
    #collision between the pairs.  Get rid of pairs that 
    #are not near each other or not in the same quadrant...
    def resolve(self, dt):
        pairDict = {}
        for pair in self.pairs:
            self.setEntityPair(*pair)
            colliding = self.calculateCollision()
            if colliding:
                if not self.entity1.radius and self.entity2.radius:
                    pairDict[pair] = self.getOverlapArea() #This is for AABBAABB collision
                else:
                    pairDict[pair] = 0 #resolve anything not AABBAABB last
        pairSorted = sorted(pairDict.items(), key=lambda x: x[1], reverse=True)
        pairs = [k[0] for k in pairSorted]
      
        for pair in pairs:
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
        vec = self.entity1.position - self.entity2.position
        distance = vec.magnitudeSquared()
        thresh = (self.entity1.radius+self.entity2.radius)**2
        if distance <= thresh:
            return True
        return False
    
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
        if self.entity1.isImpenetrable or self.entity2.isImpenetrable:
            self.separateEntities()
        self.entity1.collisionAction(self.entity2)
        self.entity2.collisionAction(self.entity1)
            
    def separateEntities(self):
        '''Separate entities that are not allowed to penetrate'''
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
            #a.addImpulse(vx=a.velocity.x*-1, vy=a.velocity.y)
        elif xOverlap == yOverlap:
            pass
        
    def resolveCircleCircle(self, dt):
        pass
    
    def resolveCircleAABB(self, dt):
        pass
    
    def resolveAABBCircle(self, dt):
        pass
       
                
    def getOverlapArea(self):
        xOverlap = self.getXOverlap(self.entity1, self.entity2)
        yOverlap = self.getYOverlap(self.entity1, self.entity2)
        return xOverlap * yOverlap
        
        
            
    def calculateSeparatingVelocity(self):
        pass
