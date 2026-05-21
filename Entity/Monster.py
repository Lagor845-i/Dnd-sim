from Components import AbilityScores, Statblock
from Entity.Creature import Creature
from Util.Vector import Vector

class Monster(Creature):
    def __init__(self, name: str, Image_id: str | None, Creature_id: str, Stats: Statblock, Ability_scores: AbilityScores, Features, Pos: Vector = Vector(0,0)) -> None:
        super().__init__(name, Image_id, Creature_id, Stats, Ability_scores, Features, Pos)