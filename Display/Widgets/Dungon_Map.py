import pygame

from Display.Widgets import WidgetBase
from Display.ScreenComponents import *

class DungeonMap2d(WidgetBase):
    def __init__(self) -> None:
        super().__init__()

    def _load_map(self,map_name:str) -> pygame.Surface:
        with open(f"\\maps\\{map_name}") as file:
            file.read()

        return pygame.Surface((0,0)) # Change this later