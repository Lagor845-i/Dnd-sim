from Display.Screens.Screen_Base import ScreenBase
from pygame import Surface

class MainMenu(ScreenBase):
    def __init__(self,window:Surface) -> None:
        super().__init__(window)
    
    def Render(self):
        self.window.fill((0,0,0))

    def DetectClicks(self,pos):
        pass