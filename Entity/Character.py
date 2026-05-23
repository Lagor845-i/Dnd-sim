from Components.Ability_Scores import AbilityScores
from Components.Features import Features
from Components.Stat_Block import Statblock
from Entity.NonPlayerCreature import NonPlayerCreature
from Util.Vector import Vector

class Charater(NonPlayerCreature):
    """DND Non playable Characters. \n
    This can include anyone with dialog like a villian or support NPC
    Will see if I can add a feature to pin them in notes."""
    def __init__(self, 
                 name: str, 
                 Backstory:str, 
                 Image_id: str | None, 
                 Creature_id: str, 
                 Creature_type:str,
                 Stats: Statblock, 
                 Ability_scores: AbilityScores, 
                 Saves:list = [], 
                 Skills:list = [], 
                 Features: Features | None = None, 
                 Pos: Vector = Vector()) -> None:
        super().__init__(name, Image_id, Creature_id, Creature_type, Stats, Ability_scores, Saves, Skills, Features, Pos)
        self._Backstory = Backstory

    def getBackstory(self):
        return self._Backstory