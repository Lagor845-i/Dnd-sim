from abc import ABC

from Components import Sight

class BaseRace():
    def __init__(self,Creature_type:str = "Humanoid",Size:str = "M",Speed:int = 30,Vision:Sight = Sight()) -> None:
        pass

    def on_turn_start(self):
        pass

    def on_turn_end(self):
        pass

    def before_attack_roll(self):
        pass

    def after_attack_roll(self):
        pass

    def before_damage(self):
        pass

    def after_damage(self):
        pass

    def before_spell_cast(self):
        pass

    def after_spell_cast(self):
        pass

    def on_short_rest(self):
        pass

    def on_long_rest(self):
        pass