import pygame
from typing import Optional

from Display.fonts import Fonts

class Text:
    def __init__(self,text:str,font:str,font_size:int,font_color:tuple,center_pos:tuple,background_color:Optional[tuple] = None) -> None:
        self.text = text
        self.font = pygame.font.Font(Fonts().fonts_list[font],font_size)
        self.font_color = font_color
        self.background_color = background_color
        self.center_pos = center_pos
        self.re_render_font(self.center_pos)

    def update_text(self,text:str):
        self.text = text
        self.re_render_font(self.center_pos)

    def re_render_font(self,center_pos):
        self.rendered_font = self.font.render(self.text,True,self.font_color,self.background_color)
        self.rect = self.rendered_font.get_rect()
        self.rect.center = center_pos

    def Render(self,surface:pygame.Surface):
        surface.blit(self.rendered_font,self.rect)