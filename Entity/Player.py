from Components.Ability_Scores import AbilityScores
from Components.Classes import BaseClass
from Entity import Creature
from Util.Vector import Vector

from System.Conditions import ConditionBase

class Player(Creature):
    def __init__(self, name: str, Image_id: str | None, Creature_id: str, Ability_scores: AbilityScores, player_class:BaseClass, Pos: Vector = Vector(0,0)) -> None:
        super().__init__(name, Image_id, Creature_id, Ability_scores, Pos)
        self._Current_hp = 0
        self._Player_class = player_class
        self._Conditions = []
    
    def setHp(self,hp:int):
        self._current_hp = hp

    def getHp(self) -> int:
        return self._current_hp
    
    def giveCondition(self,condition:ConditionBase):
        self._Conditions.append(condition)