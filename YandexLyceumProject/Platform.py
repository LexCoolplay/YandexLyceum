from pygame import Surface
from pygame import sprite
from pygame import Rect
from Util import *
import GameObject

class Platform(GameObject.GameObject):
    def __init__(self,x,y,source = None):
        self.surface = Surface((PLAT_H, PLAT_W))
        sprite.Sprite.__init__(self)
        self.rect = Rect(x,y, PLAT_H,PLAT_W)
        if source == None:
            color = (230, 30, 30)
            self.surface.fill(color)
        else:
            pass
            #DOBAV'


