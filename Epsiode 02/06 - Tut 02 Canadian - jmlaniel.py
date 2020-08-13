import pygame

WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()

screen = pygame.display.set_mode((800,400))
screen.fill(WHITE)

pygame.draw.rect(screen,RED,(0,0,200,400))
pygame.draw.rect(screen,RED,(600,0,800,400))

pygame.draw.polygon(screen,RED,((390,370),(395,290),(315,300),(325,270),(245,200),(266,195),\
(250,145),(300,150),(300,130),(355,175),(335,75),(370,90),(400,35),(430,90),(465,75),(445,175),\
(490,130),(500,150),(550,145),(535,195),(555,200),(475,270),(485,300),(405,290),(410,370)))

pygame.display.update()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()
pygame.quit()
