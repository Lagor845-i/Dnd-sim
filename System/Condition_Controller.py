from System.Gamestate import GameState
from System.Conditions.Condition_Base import ConditionBase

class ConditionController:
    def __init__(self,gamestate:GameState) -> None:
        self.gamestate = gamestate

    def Run(self,condition:ConditionBase):
        pass