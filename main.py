import pygame

from Display.Ui_State import UiState
from Display import ScreenManager
from System import GameState

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.ui_state = UiState()
        self.screen_manager = ScreenManager(self.game_state,self.ui_state)
    
    def Get_Input(self):
        self.screen_manager.Get_input()
    
    def Render(self):
        self.screen_manager.Render()
    
    def GameLoop(self):
        while self.game_state.running:
            self.Get_Input()
            if self.game_state.running:
                self.Render()
                pygame.display.update()
            self.clock.tick()
            self.ui_state.current_fps = int(self.clock.get_fps())

    def Start(self):
        self.game_state.running = True
        self.GameLoop()

Game().Start()