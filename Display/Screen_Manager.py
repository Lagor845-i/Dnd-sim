import pygame

from Display.Ui_State import UiState
from Display.Screens import *
from System import GameState

class ScreenManager():
    def __init__(self,game_state:GameState) -> None:
        self.typing = False
        self.typebuffer = []
        self.game_state = game_state
        self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
        self.ui_state = UiState()
        self.screens = {
            "MainMenu" : MainMenu(self.window),
            "SettingsMenu" : SettingsMenu(self.window),
            "CharacterMenu" : CharacterMenu(self.window),
            "MapCreator" : MapCreator(self.window),
            "InGame" : InGame(self.window),
        }

    def Render(self):
        current_screen = self.ui_state.get_current_screen()
        if current_screen == "":
            self.ui_state.change_screen("MainMenu")
        self.screens[self.ui_state.get_current_screen()].Render()

    def Get_input(self,mouse_loc,key_buffer):
        for key in key_buffer:
            if self.typing:
                if key.key == pygame.K_ESCAPE:
                    self.typing = False
                else:
                    self.typebuffer.append(key.unicode)
            else:
                if key.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()