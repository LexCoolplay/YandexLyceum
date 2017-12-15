from pygame import *
from pygame.locals import *
#from Platform import Platform
from Button import Button
from Util import *
init()

level = ["--------------------",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "-                  -",
         "--------------------"]
entities = []

display.init()
resolution = (600,800)
screen = display.set_mode(resolution,NOFRAME)
surface_b = Surface((50,50))
surface_b.fill((255,0,0))
quit_button = Button(quit_button_func,Rect((resolution[0]-50,0),(50,50)),surface_b)
entities.append(quit_button)
while True:
    for e in event.get():
        if e.type == QUIT:
            sys.exit(0)
        if e.type == MOUSEBUTTONDOWN and ((quit_button.rect.x < e.dict['pos'][0] < quit_button.rect.x+50) and (quit_button.rect.y < e.dict['pos'][1] < quit_button.rect.y+50)):
            quit_button.onclick()
        #print(e)
    for en in entities:
        en.draw(screen)
    display.update()


pygame.quit()