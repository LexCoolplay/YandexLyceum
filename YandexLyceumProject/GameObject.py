from pygame import Rect
from pygame import sprite
class GameObject(sprite.Sprite):
    def __init__(self):
        self.surface = None

        self.rect = Rect(0, 0, 0, 0)
    def draw(self, screen):
        screen.blit(self.surface,(self.rect.x,self.rect.y))
