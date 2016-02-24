from forces import *

class ForceRegistry(object):
    def __init__(self):
        self.registry = {}
    
    def add(self, entity, force):
        pass
    
    def remove(self, entity, force):
        pass
    
    def clear(self):
        self.registry = {}
    
    def updateForces(self, dt):
        pass
    
    
