from abc import ABC,abstractmethod
from typing import Optional

from .Base_Subclass import BaseSubclass

class BaseClass(ABC):
    def __init__(self,Level:int,Hit_Dice:str,Saves:list = [],Skills:list = [],Weapon_Proficiencies:list = [],Armor_Proficiencies:list = [],Subclass:Optional[BaseSubclass] = None) -> None:
        self._Level = Level
        self._Hit_Dice = Hit_Dice
        self._Saves = Saves
        self._Skills = Skills
        self._Weapon_Proficiencies = Weapon_Proficiencies
        self._Armor_Proficiencies = Armor_Proficiencies
        self.Subclass = Subclass

    def getLevel(self):
        return self._Level
    
    def getHitDice(self):
        return self._Hit_Dice

    def getSaves(self):
        return self._Saves
    
    def getSkills(self):
        return self._Skills
    
    def getWeaponProficiencies(self):
        return self._Weapon_Proficiencies
    
    def getArmorProficiencies(self):
        return self._Armor_Proficiencies
    
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