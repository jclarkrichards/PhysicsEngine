from forces import *

forceDict = {0:Gravity(), 1:Drag()}

class ForceRegistry(object):
    def __init__(self):
        self.registry = {}
        self.entities = []
        
    def addGravity(self, entity):
        if entity.ID in self.registry.keys():
            self.registry[entity.ID].append(0)
            self.entities.append(entity)
        else:
            self.registry[entity.ID] = [0]
            self.entities.append(entity)
            
    def removeGravity(self, entity):
        pass
    
    def clear(self):
        self.registry = {}
    
    def updateForces(self, dt):
        for el in self.registry.keys():
            forceVals = self.registry[el]
            for i in forceVals:
                force = forceDict[i]
                force.updateForce(self.entities[el])
    
    
