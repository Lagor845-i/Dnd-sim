from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entity import Creature

class ConditionSource:
    def __init__(self,Condition_id,Target:Creature,Source,Concentration:bool = False) -> None:
        self.Condition_id = Condition_id
        self.Target = Target
        self.Source = Source
        self.Concentration = Concentration