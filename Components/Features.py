from typing import Optional

from .Sight import Sight

class Features:
    """
    Stores all of the features of a monster, character, or creature
    """
    def __init__(self,Sight:Sight = Sight(),Resistances:Optional[list[str]] = None,Immunities:Optional[list[str]] = None,Traits:Optional[list] = None) -> None:
        self._Sight = Sight
        self._Resistances = Resistances
        self._Immunities = Immunities
        self._Traits = Traits

    def getResistances(self):
        return self._Resistances
    
    def getImmunities(self):
        return self._Immunities
    
    def getTraits(self):
        return self._Traits