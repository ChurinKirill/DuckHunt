import pygame
def move(x, y, widht, height):
    speed = 8
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x + widht < 740:
        x += speed
    #if keys[pygame.K_UP] and y > 10:
        #y -= speed
    #if keys[pygame.K_DOWN] and y + height < 340:
        #y += speed
    return x, y
def Death():
    print('You died!')