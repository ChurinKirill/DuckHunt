from random import randint
from abc import ABC, abstractmethod
from Teleport import Teleport_Bird
import pygame
class Bird(ABC):
    def __init__(self, widht, height, atlas):
        self.widht = widht
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = randint(1, 4)
        self.speed = randint(2, 6)
        self.AnimCount = randint(1, 8)
        self.Atlas = atlas
        self.IsAlive = True
    def Fly(self):
        if self.direction == 1:
            self.x += self.speed + 2
            if self.y < 5:
                self.y += 6
            elif self.y + self.height >= 187:
                self.y -= 6
            else:
                self.y += randint(-3, 3)
            #self.widht -= 0.05
            #self.height -= 0.05
        elif self.direction == 2:
            self.x += -(self.speed + 2)
            if self.y < 5:
                self.y += 6
            elif self.y + self.height >= 187:
                self.y -= 6
            else:
                self.y += randint(-3, 3)
            #self.widht -= 0.05
            #self.height -= 0.05
        elif self.direction == 3:
            self.x -= self.speed
            self.y -= self.speed
            #self.widht -= 0.05
            #self.height -= 0.05
        elif self.direction == 4:
            self.x += self.speed
            self.y -= self.speed
            #self.widht -= 0.05
            #self.height -= 0.05
    def TryTeleport(self):
        if self.direction == 1 or self.direction == 4:
            if self.x >= 750 - self.widht:
                self.speed, self.x, self.y, self.widht, self.height = Teleport_Bird(self)
        elif self.direction == 2 or self.direction == 3:
            if self.x < 5:
                self.speed, self.x, self.y, self.widht, self.height = Teleport_Bird(self)
        elif self.direction == 3 or self.direction == 4:
            if self.y < 5:
                self.speed, self.x, self.y, self.widht, self.height = Teleport_Bird(self)
    def Draw(self, window, bird, bird_x, bird_y):
        window.blit(bird, (bird_x, bird_y))
    def Sound(self):
        r = randint(1, 150)
        if r == 1:
            self.Sound1.play()
        elif r == 2:
            self.Sound2.play()
    @abstractmethod
    def Anim(self):
        pass
    @abstractmethod
    def SetSound(self):
        pass

class Duck(Bird):
    def Anim(self):
        if self.IsAlive:
            self.AnimCount += 1
            surf = pygame.Surface((50, 30), pygame.SRCALPHA, 32)
            if self.AnimCount == 1 or self.AnimCount == 7:
                surf.blit(self.Atlas, (0, 0), (230, 200, 47, 17))
            elif self.AnimCount == 2 or self.AnimCount == 6:
                surf.blit(self.Atlas, (0, 0), (302, 200, 47, 16))
            elif self.AnimCount == 3 or self.AnimCount == 5:
                surf.blit(self.Atlas, (0, 0), (13, 190, 48, 28))
            elif self.AnimCount == 4:
                surf.blit(self.Atlas, (0, 0), (87, 188, 46, 28))
            elif self.AnimCount == 8:
                self.AnimCount = 0
                surf.blit(self.Atlas, (0, 0), (158, 200, 47, 23))
        if self.direction == 2 or self.direction == 3:
            surf = pygame.transform.flip(surf, True, False)            
        return surf
    def SetSound(self):
        self.Sound1 =  pygame.mixer.Sound('Quack1.mp3')
        self.Sound2 = pygame.mixer.Sound('Quack2.mp3')

class Raven(Bird):
    def Anim(self):
        #416, 32 // 143, 112
        if self.IsAlive:
            k = 2.5
            self.AnimCount += 1
            surf = pygame.Surface((60, 60), pygame.SRCALPHA, 32)
            if self.AnimCount == 1 or self.AnimCount == 11:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(4 // k), int(4 // k), int(143 // k), int(143 // k)))
            if self.AnimCount == 2 or self.AnimCount == 10:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(416 // k), int(32 // k), int(143 // k), int(112 // k)))
            if self.AnimCount == 3 or self.AnimCount == 9:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(421 // k), int(486 // k), int(138 // k), int(66 // k)))
            if self.AnimCount == 4 or self.AnimCount == 8:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(1244 // k), int(89 // k), int(143 // k), int(55 // k)))
            if self.AnimCount == 5 or self.AnimCount == 7:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(625 // k), int(89 // k), int(139 // k), int(98 // k)))
            if self.AnimCount == 6:
                surf.blit(pygame.transform.scale(self.Atlas, (int(1803 // k), int(616 // k))), (0, 0), (int(1079 // k), int(90 // k), int(142 // k), int(113 // k)))
            if self.AnimCount == 11:
                self.AnimCount = 0
        if self.direction == 2 or self.direction == 3:
            surf = pygame.transform.flip(surf, True, False)            
        return surf
    def SetSound(self):
        self.Sound1 =  pygame.mixer.Sound('Cra.mp3')
        self.Sound2 = pygame.mixer.Sound('Cra.mp3')