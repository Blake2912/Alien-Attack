import pygame
import random
import math
from pygame import mixer


# Initialize of Pygame
pygame.init()

# Screen Creation
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Background Sound
# mixer.music.load('space_background.wav')
# mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ghost.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(30,150))
    enemyX_change.append(random.randint(2,10))
    enemyY_change.append(15)


# Bullet
# Ready, and Fire
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bulletState = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',18)
textX = 10
textY = 10

# Game over
gameOverfont = pygame.font.Font('freesansbold.ttf',50)
gameOverX = 250
gameOverY = 250

def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


def fire_bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg,(x+16,y+11))

def show_score(x,y):
    global score_value
    score = font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def isCollision(xEnemy,yEnemy,xBullet,yBullet):
    collision_dist = math.sqrt((math.pow(xEnemy - xBullet,2)) + (math.pow(yEnemy - yBullet,2)))
    if collision_dist < 32:
        return True
    else:
        return False

def game_over_text(x,y):
    game_over_txt = gameOverfont.render("GAME OVER!",True,(255,255,255))
    screen.blit(game_over_txt,(x,y))




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
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # Close on Escape
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    # Shoot Sound
                    # bullet_sound = mixer.Sound('shoot_sound.wav')
                    # bullet_sound.play()
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
    for i in range(num_of_enemies):
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(gameOverX,gameOverY)
            break

        enemyX[i] += enemyX_change[i]

        # Adding enemy game bondary
        if enemyX[i] <=0:
            enemyX_change[i] = random.randint(4,10)
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -random.randint(4,10)
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(30,150)
        
        enemy(enemyX[i],enemyY[i],i)
    
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
    
    if bulletState == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    show_score(textX,textY)

    
    player(playerX,playerY)
    pygame.display.update()