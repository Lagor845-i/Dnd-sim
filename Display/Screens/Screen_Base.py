from abc import ABC,abstractmethod
import pygame

class ScreenBase(ABC):
    def __init__(self,window:pygame.Surface) -> None:
        self.window = window

    @abstractmethod
    def Render(self):
        pass

    @abstractmethod
    def DetectClicks(self,pos):
        pass