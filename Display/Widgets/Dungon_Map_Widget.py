import pygame

class Dungeon_Map_2d():
    def __init__(self) -> None:
        pass

    def _load_map(self,map_name:str) -> pygame.Surface:
        with open(f"\\maps\\{map_name}") as file:
            file.read()

        return pygame.Surface((0,0)) # Change this later