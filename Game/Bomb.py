from random import randint
def Get_x(widht):
    return randint(5, 750 - widht - 5)
def fall(y):
    speed = 2
    return y + speed