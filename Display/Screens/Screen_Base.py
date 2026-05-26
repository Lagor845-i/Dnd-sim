from abc import ABC,abstractmethod
import pygame

from System import GameState

class ScreenBase(ABC):
    def __init__(self,change_screens) -> None:
        self.change_screens = change_screens

    @abstractmethod
    def Render(self,window:pygame.Surface,gamestate:GameState):
        pass

    @abstractmethod
    def DetectClicks(self,pos):
        pass

    @abstractmethod
    def WindowResised(self,window:pygame.Surface):
        pass

    @abstractmethod
    def MouseEffect(self,mouse_loc):
        pass
    
    @abstractmethod
    def HandleKeys(self,key_event):
        pass