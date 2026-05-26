import pygame

from Display.Screens.Screen_Base import ScreenBase
from System import GameState

class MapCreator(ScreenBase):
    def __init__(self,window:pygame.Surface,change_screens) -> None:
        super().__init__(change_screens)
    
    def Render(self,window:pygame.Surface,gamestate:GameState):
        window.fill((0,0,0))

    def DetectClicks(self,pos):
        pass

    def WindowResised(self,window:pygame.Surface):
        pass

    def MouseEffect(self,mouse_loc):
        pass

    def HandleKeys(self,key_event):
        pass