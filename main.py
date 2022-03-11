import pygame
import random


# Initialize of Pygame
pygame.init()

# Screen Creation
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

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
enemyY = random.randint(30,150)
enemyX_change = 2
enemyY_change = 20


# Bullet
# Ready, and Fire
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bulletState = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(x,y):
    screen.blit(enemyImg,(x,y))


def fire_bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg,(x+16,y+11))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Checking keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            # Close on Escape
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    

    playerX += playerX_change

    # Adding player game bondary
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    enemyX += enemyX_change

    # Adding enemy game bondary
    if enemyX <=0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change
    
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    
    if bulletState == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()