import pygame
from abc import ABC, abstractmethod
class Menu:
    def __init__(self):
        self.Music = pygame.mixer.music.load('Menu_music.ogg')
        
        pygame.font.init()
        self.Font_passive = pygame.font.SysFont('Comic Sans MS', 35)
        self.Font_active = pygame.font.SysFont('Comic Sans MS', 35, True, False)
        self.Font_results = pygame.font.SysFont('Comic Sans MS', 20)
        
        self.Volume_text = self.Font_passive.render('Volume:', True, (255, 255, 255))
        self.Volume_plus_text = self.Font_active.render('+', True, (255, 255, 255))        
        self.Volume_minus_text = self.Font_active.render('-', True, (255, 255, 255))
        
        self.Start_text_passive = self.Font_passive.render('Start', True, (255, 255, 255))
        self.Exit_text_passive = self.Font_passive.render('Exit', True, (255, 255, 255))
        self.Results_text_passive = self.Font_passive.render('Results', True, (255, 255, 255))
        self.Results_up_text_passive = self.Font_passive.render('up', True, (255, 255, 255))
        self.Results_down_text_passive = self.Font_passive.render('down', True, (255, 255, 255))
        self.Results_back_text_passive = self.Font_passive.render('back', True, (255, 255, 255))
        self.Time_text = self.Font_passive.render('Time:', True, (255, 255, 255))
        self.Time_plus_text = self.Volume_plus_text
        self.Time_minus_text = self.Volume_minus_text
    
        self.Start_text_active = self.Font_active.render('Start', True, (255, 255, 255))
        self.Exit_text_active = self.Font_active.render('Exit', True, (255, 255, 255))
        self.Results_text_active = self.Font_active.render('Results', True, (255, 255, 255))
        self.Results_up_text_active = self.Font_active.render('up', True, (255, 255, 255))
        self.Results_down_text_active = self.Font_active.render('down', True, (255, 255, 255))
        self.Results_back_text_active = self.Font_active.render('back', True, (255, 255, 255))
        
        self.Start_widht_passive, self.Start_height_passive = self.Font_passive.size('Start')
        self.Volume_plus_widht, self.Volume_plus_height = self.Font_passive.size('+')
        self.Volume_minus_widht, self.Volume_minus_height = self.Font_passive.size('-')
        self.Exit_widht_passive, self.Exit_height_passive = self.Font_passive.size('Exit')
        self.Results_text_widht, self.Results_text_height = self.Font_passive.size('Results')
        self.Results_up_text_widht, self.Results_up_text_height = self.Font_passive.size('up')
        self.Results_down_text_widht, self.Results_down_text_height = self.Font_passive.size('down')
        self.Results_back_text_widht, self.Results_back_text_height = self.Font_passive.size('back')
        self.Time_text_widht, self.Time_text_height = self.Font_passive.size('Time:')
        self.Time_plus_widht, self.Time_plus_height = self.Volume_plus_widht, self.Volume_plus_height
        self.Time_minus_widht, self.Time_minus_height = self.Volume_minus_widht, self.Volume_minus_height
        
        self.Start_x, self.Start_y = 310, 130
        self.Exit_x, self.Exit_y = 320, 190
        self.Volume_x, self.Volume_y = 0, 300
        self.Volume_plus_x, self.Volume_plus_y = 10 + self.Font_active.size('Volume:')[0], 300
        self.Volume_minus_x, self.Volume_minus_y = 20 + self.Font_active.size('Volume:')[0] + self.Font_active.size('+')[0], 300
        self.Results_text_x, self.Results_text_y = 750 - self.Results_text_widht - 10, 350 - self.Results_text_height - 10
        self.Results_up_x, self.Results_up_y = 10, 350 - self.Results_up_text_widht - 10
        self.Results_down_x, self.Results_down_y = 20 + self.Results_up_text_widht, 300
        self.Results_back_x, self.Results_back_y = 750 - self.Results_back_text_widht - 10, 300
        self.Time_text_x, self.Time_text_y = 5, 5
        self.Time_plus_x, self.Time_plus_y = 5, 5 + self.Time_text_height
        self.Time_minus_x, self.Time_minus_y = 10 + self.Time_plus_widht, 5 + self.Time_text_height
        
    def DrawText(self, window, text, text_x, text_y):
        window.blit(text, (text_x, text_y))
