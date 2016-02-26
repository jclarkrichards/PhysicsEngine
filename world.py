class World(object):
    def __init__(self):
        self.staticOBJ = {}
        self.dynamicOBJ = {}
    
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
        pass
  
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
