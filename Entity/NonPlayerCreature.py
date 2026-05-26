from CreatureComponents.Ability_Scores import AbilityScores
from CreatureComponents.Features import Features
from CreatureComponents.Stat_Block import Statblock
from Util.Vector import Vector

from .Creature import Creature
from typing import Optional

class NonPlayerCreature(Creature):
    def __init__(self, name: str, 
                 Image_id: str | None, 
                 Creature_id: str, 
                 Creature_type:str = "Humanoid",
                 Stats:Optional[Statblock] = None, 
                 Ability_scores:Optional[AbilityScores] = None, 
                 Saves:Optional[list[str]] = None, 
                 Skills:Optional[list[str]] = None,
                 Features:Optional[Features] = None, 
                 Pos: Vector = Vector(0,0)) -> None:
        Stats = Stats or Statblock(50,12,30,2)
        Saves = Saves or []
        super().__init__(name, Image_id, Creature_id, Ability_scores, Pos)
        self._Creature_type = Creature_type
        self._Stats = Stats
        self._Saves = Saves
        self._Skills = Skills
        self._Features = Features