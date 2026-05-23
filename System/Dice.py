from random import randint

class DiceManager:
    def __init__(self) -> None:
        pass

    def rolld4(self):
        return randint(1,4)
        
    def rolld6(self):
        return randint(1,6)

    def rolld8(self):
        return randint(1,8)

    def rolld10(self):
        return randint(1,10)

    def rolld12(self):
        return randint(1,12)

    def rolld20(self):
        return randint(1,20)