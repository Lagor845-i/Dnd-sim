from Components.Ability_Scores import AbilityScores
from Components.Features import Features
from Components.Stat_Block import Statblock
from Util.Vector import Vector

from .Creature import Creature
from typing import Optional

class NonPlayerCreature(Creature):
    def __init__(self, name: str, 
                 Image_id: str | None, 
                 Creature_id: str, 
                 Stats: Statblock, 
                 Ability_scores: AbilityScores, 
                 Saves:Optional[list[str]] = None, 
                 Skills:Optional[list[str]] = None,
                 Features:Optional[Features] = None, 
                 Pos: Vector = Vector(0,0)) -> None:
        super().__init__(name, Image_id, Creature_id, Ability_scores, Pos)
        self._Stats = Stats
        self._Saves = Saves
        self._Skills = Skills
        self._Features = Features