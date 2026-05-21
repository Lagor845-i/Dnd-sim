from Components import *
from Entity.Creature import Creature
from Util.Vector import Vector

class Charater(Creature):
    """DND Non playable Characters. \n
    This can include anyone with dialog like a villian or support NPC
    Will see if I can add a feature to pin them in notes."""
    def __init__(self, name: str, Backstory:str, Image_id: str | None, Creature_id: str, Stats: Statblock, Ability_scores: AbilityScores, Features:Features, Pos: Vector = Vector(0,0)) -> None:
        super().__init__(name, Image_id, Creature_id, Stats, Ability_scores, Features, Pos)
        self.Backstory = Backstory