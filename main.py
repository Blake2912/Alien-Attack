import pygame
import random
# Initialize of Pygame
pygame.init()

# Screen Creation
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Alien Attack")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("ghost.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Checking keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            # Close on Escape
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    

    playerX += playerX_change

    # Adding game bondary
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()