from Display.Screens.Screen_Base import ScreenBase
from pygame import Surface

class MapCreator(ScreenBase):
    def __init__(self,window:Surface) -> None:
        super().__init__(window)
    
    def Render(self):
        pass

    def DetectClicks(self,pos):
        pass