from Components.Speed import Speed

class Statblock():
    def __init__(self,HP:int,AC:int,Speed:Speed | int,Initiative:int) -> None:
        self.HP = HP
        self.AC = AC
        self.Speed = Speed
        self.Initiative = Initiative