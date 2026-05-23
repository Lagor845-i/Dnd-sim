from Components import AbilityScores

from Util import Vector
from typing import Optional

class Creature():
    def __init__(self,name:str,Image_id:Optional[str],Creature_id:str,Ability_scores:AbilityScores,Pos:Vector = Vector(0,0)) -> None:
        self._name = name
        self._Image_id = Image_id
        self._Creature_id = Creature_id
        self._Ability_scores = Ability_scores
        self._Pos = Pos
        self._Concentrating = False

    def getName(self):
        return self._name
    
    def getImageid(self):
        return self._Image_id
    
    def getCreatureid(self):
        return self._Creature_id
    
    def __str__(self) -> str:
        return f"{self._name} with a Creature Id of {self._Image_id}"