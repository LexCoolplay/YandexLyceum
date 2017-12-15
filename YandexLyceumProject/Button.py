from GameObject import GameObject

class Button(GameObject):
    def __init__(self, onclick_func, rect, surface):
        self.onclick = onclick_func
        self.rect = rect
        self.surface = surface
    def trigger(self):
        self.onclick()