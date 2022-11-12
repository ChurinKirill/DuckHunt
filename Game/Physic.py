import pygame
def Fall(y, height, speed):
    if y + height > 340:
        return y
    else:
        return y + speed
def move(x, y, widht, height, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:# and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT]:# and x + widht < 740:
        x += speed
    if keys[pygame.K_UP]:# and y > 10:
        y -= speed
    if keys[pygame.K_DOWN]:# and y + height < 340:
        y += speed
    return x, y
def Touch(First_x, First_y, First_height, First_widht, Second_x, Second_y, Second_widht, Second_height):
    if (First_y <= Second_y + Second_height <= First_y + First_height or First_y < Second_y) and First_x <= Second_x + Second_widht <= First_x + First_widht:
        return True
    else:
        return False