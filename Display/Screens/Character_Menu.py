import pygame
from pathlib import Path
import os

import __main__
from Display.Screens.Screen_Base import ScreenBase
from Display.ScreenComponents import Effects
from Display.ScreenComponents import Text
from Display.ScreenComponents import Button
from System import GameState

class CharacterMenu(ScreenBase):
    def __init__(self,window:pygame.Surface,change_screens) -> None:
        super().__init__(change_screens)
        self.background = pygame.image.load(Path(__main__.__file__).parent/"Game Data"/"Assets"/"Images"/"Game Images"/"Dnd sim background.jpg").convert_alpha()
        self.background = pygame.transform.smoothscale(self.background,window.get_size())
        self.background = Effects.blur_surface(self.background,5)

        window_x,window_y = window.get_size()

        self.dim_surface = pygame.Surface((window_x,window_y),pygame.SRCALPHA)
        self.dim_surface.fill((0,0,0,80))

        self.title_text = Text("Characters","KingdomCrown",70,(255,255,255),(window_x*0.5,window_y*0.2))
        self.start_button = Button("Start","KingdomCrown",40,(255,255,255),lambda:change_screens("CharacterMenu"),(window_x*0.66,window_y*0.8))
        self.not_ready_start_button = Text("Start","KingdomCrown",40,(180,180,180),(window_x*0.66,window_y*0.8))
        self.cancel_button = Button("Cancel","KingdomCrown",40,(255,255,255),lambda:change_screens("MainMenu"),(window_x*0.33,window_y*0.8))
        self.new_character_button = Button("No characters found!\nCreate Character","KingdomCrown",40,(255,255,255),lambda:change_screens("MainMenu"),(window_x*0.5,window_y*0.5))

        self.current_character = ""

        self.selected_character = None

        self.CheckForCharacters()

        if self.found_characters:
            if self.current_character == "":
                current_character_index = 0
                self.current_character = self.characters[current_character_index]

    def CheckForCharacters(self):
        character_directory = Path(__main__.__file__).parent/"Game Data"/"Characters"
        files = os.listdir(character_directory)
        self.characters = []
        if len(files) == 0:
            self.found_characters = False
        else:
            self.found_characters = True
            self.characters = files
    
    def Render(self,window:pygame.Surface,gamestate:GameState):
        window.blit(self.background,(0,0))
        self.title_text.Render(self.dim_surface)
        if self.selected_character:
            self.start_button.Render(self.dim_surface)
        else:
            self.not_ready_start_button.Render(self.dim_surface)
        self.cancel_button.Render(self.dim_surface)
        if not self.found_characters:
            self.new_character_button.Render(self.dim_surface)
        else:
            pass
        window.blit(self.dim_surface,(0,0))
        

    def DetectClicks(self,pos):
        if self.selected_character:
            self.start_button.Detect_Clicks(pos)
        self.cancel_button.Detect_Clicks(pos)

    def WindowResised(self,window:pygame.Surface):
        pass

    def MouseEffect(self,mouse_loc):
        pass

    def HandleKeys(self,key_event:pygame.event.Event):
        if key_event.key == pygame.K_RIGHT:
            if self.found_characters:
                if self.current_character == "":
                    current_character_index = round(len(self.characters)/2)-1
                    self.current_character = self.characters[current_character_index]
                else:
                    character_index = self.characters.index(self.current_character)
                    if character_index+1 <= len(self.characters)-1:
                        self.characters[character_index + 1]