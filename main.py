import pygame

# Initialize of Pygame
pygame.init()

# Screen Creation
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Alien Attack")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon) 

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
