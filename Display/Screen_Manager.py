import pygame

from Display.Ui_State import UiState
from Display.Screens import *
from System import GameState
from Display.ScreenComponents import Text

class ScreenManager():
    def __init__(self,game_state:GameState,ui_state:UiState) -> None:
        self.typing = False
        self.typebuffer = []
        self.game_state = game_state
        self.window = pygame.display.set_mode((0,0),pygame.NOFRAME | pygame.DOUBLEBUF)
        window_x,window_y = self.window.get_size()
        self.fps_counter = Text("0","KingdomCrown",32,(255,255,255),(window_x*0.95,window_y*0.05))
        pygame.display.set_caption("DnD Sim")
        self.ui_state = ui_state
        self.screens:dict[str,ScreenBase] = {
            "MainMenu" : MainMenu(self.window,self.ui_state.change_screen,game_state.stopGame),
            "SettingsMenu" : SettingsMenu(self.window,self.ui_state.change_screen),
            "CharacterMenu" : CharacterMenu(self.window,self.ui_state.change_screen),
            "MapCreator" : MapCreator(self.window,self.ui_state.change_screen),
            "InGame" : InGame(self.window,self.ui_state.change_screen),
        }

    def Render(self):
        current_screen = self.ui_state.get_current_screen()
        if current_screen == "":
            self.ui_state.change_screen("MainMenu")
        self.screens[self.ui_state.get_current_screen()].Render(self.window,self.game_state)
        if self.ui_state.fps_counter:
            self.fps_counter.update_text(f"{self.ui_state.current_fps}")
            self.fps_counter.Render(self.window)

    def Get_input(self):
        current_screen = self.ui_state.get_current_screen()
        if current_screen == "":
            self.ui_state.change_screen("MainMenu")
        if self.game_state.running:
            mouse_loc = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.ui_state.get_current_screen() == "SettingsMenu":
                        self.ui_state.change_screen("MainMenu")
                    if self.ui_state.get_current_screen() == "MainMenu":
                        self.game_state.stopGame()
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.screens[self.ui_state.get_current_screen()].DetectClicks(mouse_loc)
        
        if not self.game_state.running:
            pygame.quit()
        else:        
            self.screens[self.ui_state.get_current_screen()].MouseEffect(mouse_loc)

        