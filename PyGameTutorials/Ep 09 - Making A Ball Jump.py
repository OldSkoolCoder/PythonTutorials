import pygame

# Global Character Variables
playerX = 50
playerY = 50
playerWidth = 30
playerHeight = 30
playerVelocity = 6
screenWidth = 600
screenHeight = 400

# Colour Constants
BLUE = (0,0,255)
WHITE = (255,255,255)

# Initialising The Game Space
pygame.init() 

window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Ball Moving and jumping")

isJumping = False
jumpCounter = 10

# Game Looper
running = True
while running:

    pygame.time.delay(50) # 0.05

    # Testing For Events
    # Events Section
    for event in pygame.event.get():
        print (event)

        if event.type == pygame.QUIT:
            running = False

    # Update Section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > (playerWidth +  playerVelocity):
        playerX -= playerVelocity

    if keys[pygame.K_RIGHT] and playerX < (screenWidth - playerWidth - playerVelocity):
        playerX += playerVelocity

    if not (isJumping):
        if keys[pygame.K_UP] and playerY > (playerHeight + playerVelocity):
            playerY -= playerVelocity

        if keys[pygame.K_DOWN] and playerY < (screenHeight - playerHeight - playerVelocity):
            playerY += playerVelocity

        if keys[pygame.K_SPACE]:
            isJumping = True

    else:
        if jumpCounter >= -10:
            jumpDirection = 1
            if jumpCounter < 0:
                jumpDirection = -1

            playerY -= (jumpCounter **2) // 2 * jumpDirection
            jumpCounter -= 1
        
        else:
            isJumping = False
            jumpCounter = 10


    # Draw Section
    window.fill(WHITE)

    pygame.draw.circle(window, BLUE, (playerX,playerY) ,playerWidth, 0)

    pygame.display.flip()
    
pygame.display.quit()
pygame.quit()
