class AbilityScores():
    def __init__(self,str:int = 10,dex:int = 10,con:int = 10,inte:int = 10,wis:int = 10,cha:int = 10,Saves:list = [],Skills:list = []) -> None:
        self._str = str
        self._dex = dex
        self._con = con
        self._inte = inte
        self._wis = wis
        self._cha = cha
        self.Saves = Saves
        self.Skills = Skills

    def getstr(self) -> int:
        return self._str
    
    def getdex(self) -> int:
        return self._dex
    
    def getcon(self) -> int:
        return self._con
    
    def getint(self) -> int:
        return self._inte
    
    def getwis(self) -> int:
        return self._wis
    
    def getcha(self) -> int:
        return self._cha