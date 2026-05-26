import pygame
from pathlib import Path

import __main__
from System import GameState
from Display.Screens.Screen_Base import ScreenBase
from Display.ScreenComponents import Button
from Display.ScreenComponents import Text

class MainMenu(ScreenBase):
    def __init__(self,window:pygame.Surface,change_screens,stop_running) -> None:
        super().__init__(change_screens)
        self.on_first_load = True
        self.background = pygame.image.load(Path(__main__.__file__).parent/"Game Data"/"Assets"/"Images"/"Game Images"/"Dnd sim background.jpg").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background,window.get_size())
        window_x,window_y = window.get_size()
        self.dim_surface = pygame.Surface((window_x*0.5,window_y*0.7),pygame.SRCALPHA)
        self.dim_rect = (window_x*0.25,window_y*0.2)
        window_x,window_y = self.dim_surface.get_size()
        self.title = Text("DND SIM","KingdomCrown",70,(255,255,255),(window_x*0.5,window_y*0.2))
        self.play_button = Button("Play","KingdomCrown",40,(255,255,255),lambda:change_screens("CharacterMenu"),(window_x*0.5,window_y*0.4),self.dim_rect)
        self.create_button = Button("Create","KingdomCrown",40,(255,255,255),lambda:change_screens("MapCreator"),(window_x*0.5,window_y*0.55),self.dim_rect)
        self.settings_button = Button("Settings","KingdomCrown",40,(255,255,255),lambda:change_screens("SettingsMenu"),(window_x*0.5,window_y*0.7),self.dim_rect)
        self.quit_button = Button("Quit","KingdomCrown",40,(255,255,255),stop_running,(window_x*0.5,window_y*0.85),self.dim_rect)

    def Render(self,window:pygame.Surface,gamestate:GameState):
        window.blit(self.background,(0,0))
        if self.on_first_load:
            self.dim_surface.fill((0,0,0,80))
            self.title.Render(self.dim_surface)
            self.play_button.Render(self.dim_surface)
            self.create_button.Render(self.dim_surface)
            self.settings_button.Render(self.dim_surface)
            self.quit_button.Render(self.dim_surface)
            self.on_first_load = False
        window.blit(self.dim_surface,self.dim_rect)

    def DetectClicks(self,pos):
        self.play_button.Detect_Clicks(pos)
        self.create_button.Detect_Clicks(pos)
        self.settings_button.Detect_Clicks(pos)
        self.quit_button.Detect_Clicks(pos) # Check this last or program will crash

    def WindowResised(self,window:pygame.Surface):
        self.background = pygame.transform.smoothscale(self.background,window.get_size())

    def MouseEffect(self,mouse_loc):
        pass

    def HandleKeys(self,key_event):
        pass