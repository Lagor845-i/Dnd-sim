from Components import Statblock,AbilityScores,Features

from Util import Vector
from typing import Optional

class Creature():
    def __init__(self,name:str,Image_id:Optional[str],Creature_id:str,Stats:Statblock,Ability_scores:AbilityScores,Features:Optional[Features] = None,Pos:Vector = Vector(0,0)) -> None:
        self._name = name
        self._Image_id = Image_id
        self._Creature_id = Creature_id
        self._Stats = Stats
        self._Ability_scores = Ability_scores
        self._Features = Features
        self._Pos = Pos
        self._Concentrating = False

    def getName(self):
        return self._name
    
    def __str__(self) -> str:
        return f"{self._name} with a Creature Id of {self._Image_id}"