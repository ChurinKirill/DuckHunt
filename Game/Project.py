import pygame
import random
import time
from datetime import date, datetime

import Bird
from Teleport import Teleport_Bird
import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.Game_window = pygame.display.set_mode((750, 350))
        pygame.display.set_caption("Duck Hunt")

        self.MyFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.Reloading_Start = self.MyFont.render('Reloading...', True, (0, 0, 0))
        self.Reloading_End = self.MyFont.render('Reloading...', True, (0, 255, 0))
        
        self.Shot = pygame.mixer.Sound('Shot.mp3')
        self.Reloading = pygame.mixer.Sound('Reloading.wav')
        pygame.mixer.music.load('Menu_music.ogg')
        
        self.WeaponAtlas = pygame.image.load('WeaponAtlas.png')
        self.DuckAtlas = pygame.image.load('DuckAtlas.png')
        self.RavenAtlas = pygame.image.load('RavenAtlas.png')
        self.Scope = pygame.image.load('Scope.png')
        self.Background = pygame.image.load('Background.png')
        
        self.Scope_widht, self.Scope_height = 100, 100
        self.Ammo_Count = 8
        self.Scope_x, self.Scope_y = 375, 345 - self.Scope_height - 5
        self.Score = 0
        self.Time = 30
        self.Result_idx = -1
        self.Ducks = [Bird.Duck(48, 30, self.DuckAtlas) for i in range(10)]
        self.Ravens = [Bird.Raven(50, 50, self.RavenAtlas) for i in range(random.randint(2, 5))]
        self.Menu = Menu.Menu()
        for Duck in self.Ducks:
            Duck.SetSound()
            Duck.speed, Duck.x, Duck.y, Duck.widht, Duck.height = Teleport_Bird(Duck)
        for Raven in self.Ravens:
            Raven.SetSound()
            Raven.speed, Raven.x, Raven.y, Raven.widht, Raven.height = Teleport_Bird(Raven)
        self.Is_Reloading = False
        self.Is_Shot = False
        self.Start_Reloading = 0
        self.k = 1.5
        self.game = False
        self.menu = True
        self.results = False
        self.Music_play = True

    def Draw_gameS(self, window, text, text_x, text_y):
        window.blit(text, (text_x, text_y))
        
    def Start(self):
        while True:
            while self.menu:
                if self.Music_play:
                    pygame.mixer.music.play()
                    self.Music_play = False
                pygame.mouse.set_visible(True)
                pygame.time.delay(40)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.Menu.Start_x <= Mouse_x <= self.Menu.Start_x + self.Menu.Start_widht_passive and self.Menu.Start_y <= Mouse_y <= self.Menu.Start_y + self.Menu.Start_height_passive:
                            self.menu = False
                            self.game = True
                            self.Music_play = True
                            pygame.mixer.music.stop()
                            Timer = time.time()
                        elif self.Menu.Exit_x <= Mouse_x <= self.Menu.Exit_x + self.Menu.Exit_widht_passive and self.Menu.Exit_y <= Mouse_y <= self.Menu.Exit_y + self.Menu.Exit_height_passive:
                            self.game = False
                            self.menu = False
                            pygame.quit()
                        elif self.Menu.Volume_plus_x <= Mouse_x <= self.Menu.Volume_plus_x + self.Menu.Volume_plus_widht and self.Menu.Volume_plus_y <= Mouse_y <= self.Menu.Volume_plus_y +self. Menu.Volume_plus_height:
                            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
                        elif self.Menu.Volume_minus_x <= Mouse_x <= self.Menu.Volume_minus_x + self.Menu.Volume_minus_widht and self.Menu.Volume_minus_y <= Mouse_y <= self.Menu.Volume_minus_y + self.Menu.Volume_minus_height:
                            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
                        elif self.Menu.Results_text_x <= Mouse_x <= self.Menu.Results_text_x + self.Menu.Results_text_widht and self.Menu.Results_text_y <= Mouse_y <= self.Menu.Results_text_y + self.Menu.Results_text_height:
                            Results = open('Results.txt', 'r')
                            lines = Results.readlines()
                            if len(lines) > 0:
                                self.menu = False
                                self.results = True
                            else:
                                Results.close()
                        elif self.Menu.Time_plus_x <= Mouse_x <= self.Menu.Time_plus_x + self.Menu.Time_plus_widht and self.Menu.Time_plus_y <= Mouse_y <= self.Menu.Time_plus_y + self.Menu.Time_plus_height:
                            self.Time += 5
                        elif self.Menu.Time_minus_x <= Mouse_x <= self.Menu.Time_minus_x + self.Menu.Time_minus_widht and self.Menu.Time_minus_y <= Mouse_y <= self.Menu.Time_minus_y + self.Menu.Time_minus_height and self.Time > 5:
                            self.Time -= 5
        
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                self.Game_window.fill((0, 0, 0))
                
                if self.Menu.Start_x <= Mouse_x <= self.Menu.Start_x + self.Menu.Start_widht_passive and self.Menu.Start_y <= Mouse_y <= self.Menu.Start_y + self.Menu.Start_height_passive:
                    self.Menu.DrawText(self.Game_window, self.Menu.Start_text_active, self.Menu.Start_x, self.Menu.Start_y)
                else:
                    self.Menu.DrawText(self.Game_window, self.Menu.Start_text_passive, self.Menu.Start_x, self.Menu.Start_y)
        
                if self.Menu.Exit_x <= Mouse_x <= self.Menu.Exit_x + self.Menu.Exit_widht_passive and self.Menu.Exit_y <= Mouse_y <= self.Menu.Exit_y + self.Menu.Exit_height_passive:
                    self.Menu.DrawText(self.Game_window, self.Menu.Exit_text_active, self.Menu.Exit_x, self.Menu.Exit_y)
                else:
                    self.Menu.DrawText(self.Game_window, self.Menu.Exit_text_passive, self.Menu.Exit_x, self.Menu.Exit_y)
        
                if self.Menu.Results_text_x <= Mouse_x <= self.Menu.Results_text_x + self.Menu.Results_text_widht and self.Menu.Results_text_y <= Mouse_y <= self.Menu.Results_text_y + self.Menu.Results_text_height:
                    self.Menu.DrawText(self.Game_window, self.Menu.Results_text_active, self.Menu.Results_text_x, self.Menu.Results_text_y)
                else:
                    self.Menu.DrawText(self.Game_window, self.Menu.Results_text_passive, self.Menu.Results_text_x, self.Menu.Results_text_y)
        
                self.Menu.DrawText(self.Game_window, self.Menu.Volume_text, self.Menu.Volume_x, self.Menu.Volume_y)
                self.Menu.DrawText(self.Game_window, self.Menu.Volume_plus_text, self.Menu.Volume_plus_x, self.Menu.Volume_plus_y)
                self.Menu.DrawText(self.Game_window, self.Menu.Volume_minus_text, self.Menu.Volume_minus_x, self.Menu.Volume_minus_y)
                self.Menu.DrawText(self.Game_window, self.Menu.Time_text, self.Menu.Time_text_x, self.Menu.Time_text_y)
                Text_time = self.Menu.Font_passive.render(str(self.Time) + ' seconds', True, (255, 255, 255))
                self.Menu.DrawText(self.Game_window, Text_time, 10 + self.Menu.Time_text_widht, 5)
                self.Menu.DrawText(self.Game_window, self.Menu.Time_plus_text, self.Menu.Time_plus_x, self.Menu.Time_plus_y)
                self.Menu.DrawText(self.Game_window, self.Menu.Time_minus_text, self.Menu.Time_minus_x, self.Menu.Time_minus_y)
                pygame.display.update()
            
            while self.results:
        
                pygame.time.delay(40)
                self.Game_window.fill((0, 0, 0))
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
        
                if self.Menu.Results_up_x <= Mouse_x <= self.Menu.Results_up_x + self.Menu.Results_up_text_widht and self.Menu.Results_up_y <= Mouse_y <= self.Menu.Results_up_y + self.Menu.Results_up_text_height:
                    self.Game_window.blit(self.Menu.Results_up_text_active, (self.Menu.Results_up_x, self.Menu.Results_up_y))
                else:
                    self.Game_window.blit(self.Menu.Results_up_text_passive, (self.Menu.Results_up_x, self.Menu.Results_up_y))
                if self.Menu.Results_down_x <= Mouse_x <= self.Menu.Results_down_x + self.Menu.Results_down_text_widht and self.Menu.Results_down_y <= Mouse_y <= self.Menu.Results_down_y + self.Menu.Results_down_text_height:
                    self.Game_window.blit(self.Menu.Results_down_text_active, (self.Menu.Results_down_x, self.Menu.Results_down_y))
                else:
                    self.Game_window.blit(self.Menu.Results_down_text_passive, (self.Menu.Results_down_x, self.Menu.Results_down_y))
                if self.Menu.Results_back_x <= Mouse_x <= self.Menu.Results_back_x + self.Menu.Results_back_text_widht and self.Menu.Results_back_y <= Mouse_y <= self.Menu.Results_back_y + self.Menu.Results_back_text_height:
                    self.Game_window.blit(self.Menu.Results_back_text_active, (self.Menu.Results_back_x, self.Menu.Results_back_y))
                else:
                    self.Game_window.blit(self.Menu.Results_back_text_passive, (self.Menu.Results_back_x, self.Menu.Results_back_y))
                    
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.Menu.Results_up_x <= Mouse_x <= self.Menu.Results_up_x + self.Menu.Results_up_text_widht and self.Menu.Results_up_y <= Mouse_y <= self.Menu.Results_up_y + self.Menu.Results_up_text_height and self.Result_idx < -1:
                            self.Result_idx += 1
                        elif self.Menu.Results_down_x <= Mouse_x <= self.Menu.Results_down_x + self.Menu.Results_down_text_widht and self.Menu.Results_down_y <= Mouse_y <= self.Menu.Results_down_y + self.Menu.Results_down_text_height and self.Result_idx > -len(lines):
                            self.Result_idx -= 1
                        if self.Menu.Results_back_x <= Mouse_x <= self.Menu.Results_back_x + self.Menu.Results_back_text_widht and self.Menu.Results_back_y <= Mouse_y <= self.Menu.Results_back_y + self.Menu.Results_back_text_height:
                            Results.close()
                            self.menu = True
                            self.results = False
                            break
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            self.Result_idx += 1
                        if event.key == pygame.K_DOWN:
                            self.Result_idx -= 1
                Result = self.Menu.Font_results.render(lines[self.Result_idx][:-1], True, (255, 255, 255))
                self.Game_window.blit(Result, (50, 150))
                pygame.display.update()
            
            while self.game:
        
                pygame.mouse.set_visible(False)    
                pygame.time.delay(40)
                if int(time.time() - Timer) == self.Time:
                    self.Game_window.fill((0, 0, 0))
                    TimeOut = self.MyFont.render('Time Out!', True, (255, 255, 255))
                    self.Game_window.blit(TimeOut, (300, 160))
                    pygame.display.update()
                    with open('Results.txt', 'a') as Results:
                        now = datetime.now()
                        Results.write('Date: ' + str(now) + ' Time: ' + str(self.Time) + ' seconds ' + ' Score: ' + str(self.Score) + '\n')
                    pygame.time.delay(5000)
                    self.game = False
                    self.menu = True
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            self.game = False
                            self.menu = True
                            break
                    if event.type == pygame.MOUSEBUTTONUP and not self.Is_Reloading:
                        self.Shot.play()
                        self.Is_Shot = True
                        for Duck in self.Ducks:
                            if Duck.x <= self.Scope_x <= Duck.x + Duck.height and Duck.y <= self.Scope_y <= Duck.y + Duck.height:
                                Duck.speed, Duck.x, Duck.y, Duck.widht, Duck.height = Teleport_Bird(Duck)
                                self.Score += 1
                        for Raven in self.Ravens:
                            if Raven.x <= self.Scope_x <= Raven.x + Raven.height and Raven.y <= self.Scope_y <= Raven.y + Raven.height:
                                Raven.speed, Raven.x, Raven.y, Raven.widht, Raven.height = Teleport_Bird(Raven)
                                self.Score -= 2
                        self.Ammo_Count -= 1
                self.Scope_x, self.Scope_y = pygame.mouse.get_pos()
                for Raven in self.Ravens:
                    Raven.Fly()
                    Raven.TryTeleport()
                for Duck in self.Ducks:
                    Duck.Fly()
                    Duck.TryTeleport()
                Text_Score = self.MyFont.render('Score: ' + str(self.Score), True, (0, 0, 0))
                Text_ammo = self.MyFont.render('Ammo: ' + str(self.Ammo_Count) + '/8', True, (0, 0, 0))
                self.Draw_gameS(self.Game_window, pygame.transform.scale(self.Background, (750, 350)), 0, 0)
                for Duck in self.Ducks:
                    Raven.Draw(self.Game_window, Duck.Anim(), Duck.x, Duck.y)
                    Duck.Sound()
                for Raven in self.Ravens:
                    Raven.Draw(self.Game_window, Raven.Anim(), Raven.x, Raven.y)
                    Raven.Sound()
                if self.Ammo_Count == 0 and not self.Is_Reloading:
                    self.Is_Reloading = True
                    self.Start_Reloading = time.time()
                    self.Reloading.play()
                if int(time.time() - self.Start_Reloading) == 3:
                    self.Is_Reloading = False
                    self.Ammo_Count = 8
                if self.Is_Reloading:
                    self.Draw_gameS(self.Game_window, self.Reloading_Start, 595, 265)
                    self.Game_window.blit(pygame.transform.scale(self.WeaponAtlas, (int(919 * self.k), int(735 * self.k))), (375 - 65, 350 - 63 * self.k), (int(14 * self.k), int(21 * self.k), int(57 * self.k), int(63 * self.k)))

                self.Game_window.blit(pygame.transform.scale(self.Scope, (self.Scope_widht, self.Scope_height)), (self.Scope_x - self.Scope_widht / 2, self.Scope_y - self.Scope_height / 2, self.Scope_widht, self.Scope_height))
                self.Draw_gameS(self.Game_window, Text_Score, 0, 300)
                self.Draw_gameS(self.Game_window, Text_ammo, 595, 300)
                if self.Is_Shot:
                    self.Game_window.blit(pygame.transform.scale(self.WeaponAtlas, (int(919 * self.k), int(735 * self.k))), (375 - 65, 227), (int(231 * self.k), int(0 * self.k), int(61 * self.k), int(83 * self.k)))
                    self.Is_Shot = False
                elif not self.Is_Reloading:
                    self.Game_window.blit(pygame.transform.scale(self.WeaponAtlas, (int(919 * self.k), int(735 * self.k))), (375 - 65, 227), (int(350 * self.k), int(0 * self.k), int(61 * self.k), int(83 * self.k)))
                pygame.display.update()

            if not self.menu and not self.game:
                break
Game = Game()
Game.Start()