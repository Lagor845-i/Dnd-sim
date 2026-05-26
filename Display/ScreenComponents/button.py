import pygame
from typing import Optional

from Display.fonts import Fonts

class Button:
    def __init__(self,text:str,font:str,font_size:int,font_color:tuple,action,center_pos:tuple,surface_loc:tuple = (0,0),background_color:Optional[tuple] = None) -> None:
        self.text = text
        self.font = pygame.font.Font(Fonts().fonts_list[font],font_size)
        self.font_color = font_color
        self.background_color = background_color
        self.action = action
        self.center_pos = center_pos
        self.re_render_font(self.center_pos,surface_loc)
        

    def re_render_font(self,center_pos,surface_loc):
        self.rendered_font = self.font.render(self.text,True,self.font_color,self.background_color)
        self.rect = self.rendered_font.get_rect()
        self.rect.center = center_pos
        self.button_rect = pygame.Rect((surface_loc[0] + self.rect.left,surface_loc[1] + self.rect.top),(self.rect.width,self.rect.height))

    def Render(self,surface:pygame.Surface):
        surface.blit(self.rendered_font,self.rect)

    def Detect_Clicks(self,pos):
        if self.button_rect.collidepoint(pos):
            self.action()