from Components.Ability_Scores import AbilityScores
from Components.Stat_Block import Statblock
from Entity import Creature
from Util.Vector import Vector

class Player(Creature):
    def __init__(self, name: str, Image_id: str | None, Creature_id: str, Stats: Statblock, Ability_scores: AbilityScores, Features, Pos: Vector = Vector(0,0)) -> None:
        super().__init__(name, Image_id, Creature_id, Stats, Ability_scores, Features, Pos)