import qrcode
from io import BytesIO
from socket import gethostbyname,gethostname
import pygame

from Display.Widgets import WidgetBase
from Display.ScreenComponents import *

class JoinQRCode(WidgetBase):
    def __init__(self) -> None:
        self.refresh_qr_code()

    def refresh_qr_code(self) -> pygame.Surface:
        buffer = BytesIO()
        code = qrcode.make(f"{gethostbyname(gethostname())}:")
        code.save(buffer,"PNG")
        buffer.seek(0)
        self.qrcode = pygame.image.load(buffer).convert_alpha()
        return self.qrcode

    def get_qr_code(self) -> pygame.Surface:
        return self.qrcode
