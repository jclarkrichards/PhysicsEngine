class World(object):
  def __init__(self):
    self.staticOBJ = {}
    self.dynamicOBJ = {}
    
  def __addObject__(self, object):
    pass
    
  def addStaticObject(self, object):
    pass
  
  def addDynamicObject(self, object):
    pass
  
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
