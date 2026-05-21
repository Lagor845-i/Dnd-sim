import pygame

class Screen_Manager():
    def __init__(self) -> None:
        self.typing = False
        self.typebuffer = []

    def Render(self):
        pass

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