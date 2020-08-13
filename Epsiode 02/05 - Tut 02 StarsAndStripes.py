import pygame

def Draw5Star(x,y,w):
    pygame.draw.polygon(screen,WHITE,(
        (x+(w*.5),y),
        (x+(w*.6),y+(w*.4)),
        (x+w,y+(w*.4)),
        (x+(w*.7),y+(w*.6)),
        (x+(w*.8),y+w),
        (x+(w*.5),y+(w*.75)),
        (x+(w*.2),y+w),
        (x+(w*.3),y+(w*.6)),
        (x,y+(w*.4)),
        (x+(w*.4),y+(w*.4))
        ))



WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 337

pygame.init() 

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Draw5Star(10,10,300) #Test Star on its own

screen.fill(WHITE)

bar_height=SCREEN_HEIGHT // 13
for y in range(0,13,2):
    pygame.draw.rect(screen,RED,(0,(bar_height*y),SCREEN_WIDTH,bar_height))
    pygame.display.update()

pygame.draw.rect(screen,BLUE,(0,0, SCREEN_WIDTH * .4,(bar_height*7)))

star_h = (bar_height*7) // 10
star_w = (SCREEN_WIDTH * .4) // 12
star_h_s = star_h *.5
star_w_s = star_w * .5

for y in range (0, 5):
    for x in range(6):
        #Draw_Star(10+x*20,star_y)
        Draw5Star((star_w_s + (x*(star_w*2))),(star_h_s + (y * (star_h*2))),star_w)
for y in range (0, 4):
    for x in range(5):
        #Draw_Star(10+x*20,star_y)
        Draw5Star(((star_w_s + star_w) + (x*(star_w*2))),((star_h_s + star_h) + (y * (star_h*2))),star_w)

pygame.display.update()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()
pygame.quit()