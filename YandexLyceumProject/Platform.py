from pygame import Surface
from pygame import image
import GameObject

class Platform(GameObject):
    def __init__(self,rect,source = None):
        self.surface = Surface((rect.x,rect.y))
        self. rect = rect
        if source == None:
            color = (230, 30, 30)
            self.surface.fill(color)
        else:
            pass
            #DOBAV'


