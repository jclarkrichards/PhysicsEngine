from collisionResolver import EntityCollisionResolver

class World(object):
    def __init__(self):
        self.staticOBJ = {}
        self.dynamicOBJ = {}
        self.collisionResolver = EntityCollisionResolver()
    
    def __addObject__(self, database, obj):
        if obj.ID in database.keys():
             return
        if len(database) == 0:
            obj.setID(0)
            database[0] = obj
            return
        newID = max(database.keys()) + 1
        obj.setID(newID)
        database[newID] = obj
     
    def addStaticObject(self, obj):
        self.__addObject__(self.staticOBJ, obj)
  
    def addDynamicObject(self, obj):
        self.__addObject__(self.dynamicOBJ, obj)
        
    def __removeObject__(self, database, obj):
        if obj.ID not in database.keys():
            return
        if len(database) == 0:
            return
        removedEntity = database.pop(obj.ID)
  
    def removeStaticObject(self, obj):
        self.__removeObject__(self.staticOBJ, obj)
  
    def removeDynamicObject(self, obj):
        self.__removeObject__(self.dynamicOBJ, obj)
  
    def update(self, dt):
        for item in self.staticOBJ.values():
            item.update(dt)
        for item in self.dynamicOBJ.values():
            item.update(dt)
  
    def integrateObjects(self, dt):
        self.update(dt)
        self.resolveCollisions(dt)
    
    def setContactingPairs(self):
        '''Find all possible pairing combinations of static and dynamic objects'''
        pairs = []
        if len(self.staticOBJ) > 0:
            for item1 in self.dynamicOBJ.values():
                for item2 in self.staticOBJ.values():
                    pairs.append((item1, item2))
        dynamics = self.dynamicOBJ.values()
        for i, item in enumerate(dynamics):
            subset = dynamics[i+1:]
            for sub in subset:
                pairs.append((item, sub))
        return pairs
        
    def resolveCollisions(self, dt):
        '''Loop through the possible collision pairs and check for collisions'''
        pairs = self.setContactingPairs()
        for pair in pairs:
            self.collisionResolver.setEntities(pair)
            self.collisionResolver.resolve(dt)
  
    def clearStaticObjects(self):
        self.staticOBJ = {}
  
    def clearDynamicObjects(self):
        self.dynamicOBJ = {}
  
    def clear(self):
        self.clearStaticObjects()
        self.clearDynamicObjects()
  
    def render(self, screen):
        for item in self.staticOBJ.values():
            item.render(screen)
        for item in self.dynamicOBJ.values():
            item.render(screen)
