from abc import ABC,abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from CreatureComponents.Classes import BaseClass

class BaseSubclass(ABC):
    def __init__(self,ParentClass) -> None:
        self.ParentClass = ParentClass
    
    def event_handler(self,event):
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