import pygame

def Draw_Star(x,y):
    w=8
    pygame.draw.polygon(screen,WHITE,((x,y),(x+w,y+w),(x-w,y+w),(x,y)))
    pygame.draw.polygon(screen,WHITE,((x,y+w+w/2),(x-w,y+w/2),(x+w,y+w/2),(x,y+w+w/2)))

def Draw5Star(x,y):
    w=8
    pygame.draw.polygon(screen,WHITE,((x+(w*.5),y),(x+(w*.75),y+w),(x,y+(w*.333)),(x+w,y+(w*.333)),(x+(w*.25),y+w)))

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init() 

screen = pygame.display.set_mode((600,400))
screen.fill(WHITE)

star_y=0
H=14
for x in range(7):
    pygame.draw.rect(screen,RED,(0,star_y,400,star_y+H))
    pygame.draw.rect(screen,WHITE,(0,star_y+H,400,star_y+H*2))
    star_y+=H*2

pygame.draw.rect(screen,BLUE,(0,0,120,98))
star_y=0
for y in range (4):
    for x in range(6):
        #Draw_Star(10+x*20,star_y)
        Draw5Star(10+x*20,star_y)
    for x in range(5):
        #Draw_Star(20+x*20,star_y+10)
        Draw5Star(20+x*20,star_y+10)
    for x in range(6):
        #Draw_Star(10+x*20,star_y)
        Draw5Star(20+x*20,star_y+10)
    star_y+=20

pygame.display.update()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()
pygame.quit()