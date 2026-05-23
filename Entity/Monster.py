from Components.Ability_Scores import AbilityScores
from Components.Features import Features
from Components.Stat_Block import Statblock
from Entity.NonPlayerCreature import NonPlayerCreature
from Util.Vector import Vector

class Monster(NonPlayerCreature):
    """Creatures that are used to attack the players but dont have an explained backstory"""
    def __init__(self, name: str, Image_id: str | None, Creature_id: str, Stats: Statblock, Ability_scores: AbilityScores, Saves:list = [], Skills:list = [], Features: Features | None = None, Traits: list | None = None, Pos: Vector = Vector()) -> None:
        super().__init__(name, Image_id, Creature_id, Stats, Ability_scores, Saves, Skills, Features, Pos)