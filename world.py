class World(object):
    def __init__(self):
        self.staticOBJ = {}
        self.dynamicOBJ = {}
    
    def __addObject__(self, database, object):
        if object.ID in database.keys():
             return
        if len(database) == 0:
            database[0] = object
            return
        newID = max(database.keys()) + 1
        object.ID = newID
        database[newID] = object
     
    def addStaticObject(self, object):
        self.__addObject__(self.staticOBJ, object)
  
    def addDynamicObject(self, object):
        self.__addObject__(self.dynamicOBJ, object)
  
    def removeStaticObject(self, object):
        pass
  
    def removeDynamicObject(self, object):
        pass
  
    def update(self, dt):
        pass
  
    def integrateObjects(self, dt):
        pass
  
    def clearStaticObjects(self):
        pass
  
    def clearDynamicObjects(self):
        pass
  
    def clear(self):
        pass
  
    def render(self, screen):
        pass
