from random import randint
def Teleport_Bird(bird):
    x, y = 0, 0
    speed = randint(2, 5)
    if bird.direction == 1:
        x = 5
        y = randint(5, 15)
    elif bird.direction == 2:
        x = 750 - bird.widht - 5
        y = randint(5, 15)
    else:
        x = randint(50, 680)
        y = 225
    return speed, x, y, 48, 30