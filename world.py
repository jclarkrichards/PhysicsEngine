"""Static objects don't collide among themselves, 
Dynamic objects collide with themselves and static objects,
Other objects don't collide with anything"""

import pygame
from collisionResolver import EntityCollisionResolver
from pygame.locals import *

class World(object):
    def __init__(self):
        self.staticOBJ = {}
        self.dynamicOBJ = {}
        self.otherOBJ = {} 
        self.collisionResolver = EntityCollisionResolver()
        self.screenSize = (0, 0)
        self.screen = None
        self.background = None
        
    def setup(self, x, y):
        '''Initialize pygame and set the screen size'''
        pygame.init()
        self.screen = self.setScreenSize(x, y)
        self.setBackground()
        
    def setScreenSize(self, screenX, screenY):
        self.screenSize = (screenX, screenY)
        return pygame.display.set_mode(self.screenSize, 0, 32)
        
    def setBackground(self):
        self.background = pygame.surface.Surface(self.screenSize).convert()
        self.background.fill((10,0,60))
    
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
    
    def addOtherObject(self, obj):
        self.__addObject__(self.otherOBJ, obj)
        
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
        
    def removeOtherObject(self, obj):
        self.__removeObject__(self.otherOBJ, obj)
  
    def update(self, dt):
        for item in self.staticOBJ.values():
            item.update(dt)
        for item in self.dynamicOBJ.values():
            item.update(dt)
        for item in self.otherOBJ.values():
            item.update(dt)
  
    def integrateObjects(self, dt):
        self.update(dt)
        self.resolveCollisions(dt)
    
    def setContactingPairs(self):
        '''Find all possible pairings of static and dynamic objects'''
        if len(self.staticOBJ) > 0:
            for item1 in self.dynamicOBJ.values():
                for item2 in self.staticOBJ.values():
                    self.collisionResolver.addPair((item1, item2))
                      
        dynamics = self.dynamicOBJ.values()
        for i, item in enumerate(dynamics):
            subset = dynamics[i+1:]
            for sub in subset:
                self.collisionResolver.addPair((item, sub))
          
    def resolveCollisions(self, dt):
        '''Loop through the possible pairs and check for collisions'''
        self.setContactingPairs()
        self.collisionResolver.resolve(dt)
   
    def clearStaticObjects(self):
        self.staticOBJ = {}
  
    def clearDynamicObjects(self):
        self.dynamicOBJ = {}
        
    def clearOtherObjects(self):
        self.otherOBJ = {}
  
    def clear(self):
        self.clearStaticObjects()
        self.clearDynamicObjects()
        self.clearOtherObjects()
  
    def handleEvents(self):
        '''Event handling.  keyboard and/or mouse inputs'''
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            
    def render(self):
        self.screen.blit(self.background, (0,0))
        for item in self.staticOBJ.values():
            item.render(self.screen)
        for item in self.dynamicOBJ.values():
            item.render(self.screen)
        for item in self.otherOBJ.values():
            item.render(self.screen)
