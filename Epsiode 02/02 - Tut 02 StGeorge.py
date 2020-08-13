import pygame

WHITE = (255,255,255)
RED = (255,0,0)

pygame.init() 

screen = pygame.display.set_mode((600,400))
screen.fill(WHITE)

pygame.draw.rect(screen, RED,(270,0,60,400))
pygame.draw.rect(screen, RED,(0,170,600,60))

pygame.display.update()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

pygame.display.quit()
pygame.quit()
