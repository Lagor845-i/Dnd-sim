import pygame
from pathlib import Path

import __main__
from Display.Screens.Screen_Base import ScreenBase
from System import GameState

class SettingsMenu(ScreenBase):
    def __init__(self,window:pygame.Surface,change_screens) -> None:
        super().__init__(change_screens)
        self.background = pygame.image.load(Path(__main__.__file__).parent/"Game Data"/"Assets"/"Images"/"Game Images"/"Dnd sim background.jpg").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background,window.get_size())
        self.settings_display = pygame.Surface((300, 200), pygame.SRCALPHA)

    def Render(self,window:pygame.Surface,gamestate:GameState):
        window.blit(self.background,(0,0))
        self.settings_display.fill((0, 0, 0, 80))
        window.blit(self.settings_display,(0,0)) # Blit after filling settings.
        
        

    def DetectClicks(self,pos):
        pass

    def WindowResised(self,window:pygame.Surface):
        pass

    def MouseEffect(self,mouse_loc):
        pass