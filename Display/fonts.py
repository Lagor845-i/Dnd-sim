from pathlib import Path

class Fonts:
    def __init__(self) -> None:
        GAME_DIRECTORY = Path(__file__).resolve().parent.parent
        self.fonts_list = {
            "KingdomCrown" : GAME_DIRECTORY / "Game Data" / "Assets" / "Fonts" / "KingdomCrown" / "KingdomCrown.otf",
        }