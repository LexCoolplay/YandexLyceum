from Util import *
from pygame import Rect
from pygame import Surface
from pygame import sprite
from GameObject import GameObject





class Living(GameObject):
    def __init__(self,x,y):
        self.startX=x
        self.xvel = 0
        sprite.Sprite.__init__(self)
        self.yvel = 0
        self.startY=y
        self.rect = Rect((x,y),(PLAT_W,PLAT_H))
        self.surface =  Surface((PLAT_W,PLAT_H))
    def update(self,movement,platforms):
        self.xvel+=movement[0]
        self.rect.x+=self.xvel
        self.collide(platforms)
        self.xvel=0
        self.yvel += movement[1]
        self.rect.y+=self.yvel
        self.collide(platforms)
        self.yvel=0
    def collide(self,platforms):
        for pl in platforms:
            if(sprite.collide_rect(self,pl)):

                if(self.xvel>0):
                    self.rect.right=pl.rect.left
                if(self.xvel<0):
                    self.rect.left=pl.rect.right
                if(self.yvel>0):
                    self.rect.bottom=pl.rect.top
                if(self.yvel<0):
                    self.rect.top=pl.rect.bottom

