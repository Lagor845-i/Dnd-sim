from typing import Optional

class Sight:
    def __init__(self,Vision:bool = True,
                 Darkvision:Optional[int] = None,
                 Superior_Darkvision:Optional[int] = None,
                 Blindsight:Optional[int] = None,
                 Tremorsense:Optional[int] = None,
                 Truesight:Optional[int] = None,
                 Devils_sight:Optional[int] = None,
                 Echolocation:Optional[int] = None,
                 Witch_sight:Optional[int] = None,
                 Etherial_sight:Optional[int] = None,) -> None:
        self.Vision = Vision
        self.Darkvision = Darkvision
        self.Superior_Darkvision = Superior_Darkvision
        self.Blindsight = Blindsight
        self.Tremorsense = Tremorsense
        self.Truesight = Truesight
        self.Devils_sight = Devils_sight
        self.Echolocation = Echolocation
        self.Witch_sight = Witch_sight
        self.Etherial_sight = Etherial_sight