from pygame import Rect
class GameObject:
    def __init__(self):
        self.surface = None
        self.rect = Rect(0, 0, 0, 0)
    def draw(self, screen):
        screen.blit(self.surface,(self.rect.x,self.rect.y))
