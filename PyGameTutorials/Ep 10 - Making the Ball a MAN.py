import pygame

# Global Character Variables
playerX = 50
playerY = 535
playerWidth = 64
playerHeight = 64
playerVelocity = 6
screenWidth = 1000
screenHeight = 705

# Colour Constants
BLUE = (0,0,255)
WHITE = (255,255,255)

# Initialising The Game Space
pygame.init() 

window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Ball Moving and jumping")

clock= pygame.time.Clock()

# Load Images for the Game
background = pygame.image.load('Assets/BackGround.png')

walkingAnimation = {}
walkingAnimation['Right'] = []
walkingAnimation['Left'] = []

for i in range(1,10):
    filename = 'Assets/R{}.png'.format(i)
    imageRight = pygame.image.load(filename).convert()
    walkingAnimation['Right'].append(imageRight)

    filename = 'Assets/L{}.png'.format(i)
    imageRight = pygame.image.load(filename).convert()
    walkingAnimation['Left'].append(imageRight)

standingImage = pygame.image.load('Assets/F9.png').convert()

isJumping = False
jumpCounter = 10

walkingCounter = 0
walkingDirection = ""

characterImage = standingImage

# Game Looper
running = True
while running:

    clock.tick(27)

    # Testing For Events
    # Events Section
    for event in pygame.event.get():
        print (event)

        if event.type == pygame.QUIT:
            running = False

    # Update Section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > playerVelocity:
        playerX -= playerVelocity
        walkingDirection = 'Left'
    elif keys[pygame.K_RIGHT] and playerX < (screenWidth - playerWidth - playerVelocity):
        playerX += playerVelocity
        walkingDirection = 'Right'
    else:
        walkingDirection = ''
        walkingCounter = 0

    if not (isJumping):
        #if keys[pygame.K_UP] and playerY > (playerHeight + playerVelocity):
        #    playerY -= playerVelocity
        
        #if keys[pygame.K_DOWN] and playerY < (screenHeight - playerHeight - playerVelocity):
        #    playerY += playerVelocity

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

    if walkingCounter + 1 > 27 :
        walkingCounter = 0

    if walkingDirection != '':
        characterImage = walkingAnimation[walkingDirection][walkingCounter // 3]
        walkingCounter += 1
    else:
        characterImage = standingImage
        # walkingCounter = 0


    # Draw Section
    window.blit(background, (0,0))
    window.blit(characterImage, (playerX, playerY))

    #pygame.draw.circle(window, BLUE, (playerX,playerY) ,playerWidth, 0)

    pygame.display.flip()
    
pygame.display.quit()
pygame.quit()
