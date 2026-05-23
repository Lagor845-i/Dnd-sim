import pygame
from Display import Screen_Manager
from System import GameState

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN | pygame.DOUBLEBUF)
        self.game_state = GameState()
        self.screen_manager = Screen_Manager(self.game_state)
    
    def Get_Input(self):
        key_buffer = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_buffer.append(event)
        self.mouse_loc = pygame.mouse.get_pos()
        self.screen_manager.Get_input(self.mouse_loc,key_buffer)
    
    def Render(self):
        self.screen_manager.Render()
    
    def GameLoop(self):
        while self.running:
            self.Get_Input()
            self.Render()
            pygame.display.update()

    def Start(self):
        self.running = True
        self.GameLoop()

Game().Start()