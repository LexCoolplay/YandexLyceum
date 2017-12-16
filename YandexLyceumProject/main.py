from pygame import *
from pygame.locals import *
from Platform import Platform
from Button import Button
from Util import *
from Hero import Hero
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
screen = display.set_mode( (0,0),NOFRAME|FULLSCREEN)


hero = Hero(32,32)
entities.append(hero)
platforms=[]

for i in range(len(level)):
    for j in range(len(level[i])):
        if level[i][j]=='-':
            plat = Platform(i*PLAT_H,j*PLAT_W)
            entities.append(plat)
            platforms.append(platforms)

surface_b = Surface((50,50))
surface_b.fill((255,0,0))
screen.fill(Color(255,255,255))
quit_button = Button(quit_button_func,Rect((screen.get_rect().right-50,screen.get_rect().top),(50,50)),surface_b)
entities.append(quit_button)

living=[hero]

while True:
    for e in event.get():
        if e.type == QUIT:
            sys.exit(0)
        if e.type == MOUSEBUTTONDOWN and ((quit_button.rect.x < e.dict['pos'][0] < quit_button.rect.x+50) and (quit_button.rect.y < e.dict['pos'][1] < quit_button.rect.y+50)):
            pygame.quit()
            quit_button.onclick()
        if e.type == KEYDOWN and e.key == K_UP:
            movement[1] = -MOVESPEED
        if e.type == KEYDOWN and e.key == K_DOWN:
            movement[1] = MOVESPEED
        if e.type == KEYDOWN and e.key == K_LEFT:
            movement[0] = -MOVESPEED
        if e.type == KEYDOWN and e.key == K_RIGHT:
            movement[0] = +MOVESPEED
        if e.type == KEYUP and e.key == K_UP:
            movement[1] = -MOVESPEED
        if e.type == KEYUP and e.key == K_DOWN:
            movement[1] = +MOVESPEED
        if e.type == KEYUP and e.key == K_LEFT:
            movement[0] += MOVESPEED
        if e.type == KEYUP and e.key == K_RIGHT:
            movement[0] += -MOVESPEED
        #print(e)
    for i in living:
        i.update(movement,platforms)
    for en in entities:
        en.draw(screen)
    display.update()


