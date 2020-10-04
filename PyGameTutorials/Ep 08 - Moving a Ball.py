import pygame

# Initialising The Game Space
pygame.init() 

window = pygame.display.set_mode((600,400))
pygame.display.set_caption("Ball Moving")

# Global Character Variables
playerX = 50
playerY = 50
playerWidth = 30
playerHeight = 30
playerVelocity = 3

# Colour Constants
BLUE = (0,0,255)
WHITE = (255,255,255)

# Game Looper
running = True
while running:

    # Testing For Events
    # Events Section
    for event in pygame.event.get():
        print (event)

        if event.type == pygame.QUIT:
            running = False

    # Update Section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= playerVelocity

    if keys[pygame.K_RIGHT]:
        playerX += playerVelocity

    if keys[pygame.K_UP]:
        playerY -= playerVelocity

    if keys[pygame.K_DOWN]:
        playerY += playerVelocity

    # Draw Section
    window.fill(WHITE)

    pygame.draw.circle(window, BLUE, (playerX,playerY) ,playerWidth, 0)

    pygame.display.flip()
    
pygame.display.quit()
pygame.quit()
