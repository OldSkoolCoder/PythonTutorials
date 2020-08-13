import pygame

WHITE =(255,255,255)
RED = (255,0,0)
BLUE =(0,0,255)

pygame.init()

screen = pygame.display.set_mode((741,390))
screen.fill(WHITE)

##pygame.draw.rect(screen, RED,(270,0,60,400))
pygame.draw.rect(screen, RED,(296,0,741,30))

pygame.draw.rect(screen, RED,(296,60,741,30))

pygame.draw.rect(screen, RED,(296,120,741,30))

pygame.draw.rect(screen, RED,(296,180,741,30))

pygame.draw.rect(screen, BLUE,(0,0,296,210))

pygame.draw.rect(screen, RED,(0,240,741,30))

pygame.draw.rect(screen, RED,(0,300,741,30))

pygame.draw.rect(screen, RED,(0,360,741,30))

pygame.draw.lines(screen,(WHITE), True, ((20,10), (30,40), (8,23), (32,23), (10,40)), 4)


##pygame.draw.rect(screen, RED,(0,390,741,30))
#pygame.draw.polygon(screen,WHITE,((40,0),(600,360),(600,400),(560,400),(0,40),(0,0)))
#pygame.draw.polygon(screen,WHITE,((0,360),(560,0),(600,0),(600,40),(40,400),(0,400)))

pygame.display.update()

run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()
pygame.quit()