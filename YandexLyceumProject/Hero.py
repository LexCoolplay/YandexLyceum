from Living import Living
from pygame import Color
class Hero(Living):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.surface.fill(Color(0,255,0))
    def control(self,movement,platforms):
        self.update(movement,platforms)
