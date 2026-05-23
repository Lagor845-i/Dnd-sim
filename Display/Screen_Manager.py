import pygame
from System import GameState
from Display import UiState

class Screen_Manager():
    def __init__(self,game_state:GameState) -> None:
        self.typing = False
        self.typebuffer = []
        self.game_state = game_state
        self.ui_state = UiState()

    def Render(self):
        

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