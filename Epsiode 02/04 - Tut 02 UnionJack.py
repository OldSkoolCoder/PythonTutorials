import pygame


# Produces the Union Jack Flag.
RED = (255,0,0)
WHITE =(255,255,255)
BLUE = (0,0,255)

pygame.init()

window=pygame.display.set_mode((600,400))
# Blue Background
window.fill(BLUE)

#White Diagnols
pygame.draw.polygon(window,WHITE,((40,0),(600,370),(600,400),(550,400),(0,30),(0,0)))
pygame.draw.polygon(window,WHITE,((0,370),(550,0),(600,0),(600,30),(40,400),(0,400)))
    
#pygame.draw.polygon(window,(255,0,0),((600,0),(330,200),(300,200),(570,0),(600,0)))

# Red Diagnols
pygame.draw.polygon(window,RED,((0,0),(300,200),(270,200),(0,20),(0,0)))
pygame.draw.polygon(window,RED,((600,0),(300,200),(270,200),(570,0),(600,0)))

pygame.draw.polygon(window,RED,((600,400),(300,200),(330,200),(600,380),(600,400)))
pygame.draw.polygon(window,RED,((0,400),(300,200),(330,200),(30,400),(0,400)))

# White Cross
pygame.draw.rect(window,WHITE,(250,0,100,400))
pygame.draw.rect(window,WHITE,(0,150,600,100))

# Red Cross
pygame.draw.rect(window,RED,(270,0,60,400))
pygame.draw.rect(window,RED,(0,170,600,60))

pygame.display.update()
    
Run = True
while Run:

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            Run = False
    
pygame.display.quit()
pygame.quit()    
    