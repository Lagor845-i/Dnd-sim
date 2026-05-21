from System.Conditions.Condition_Base import Condition

class Poisoned(Condition):
    def __init__(self, duration: int, target: str, giver: str) -> None:
        super().__init__(duration, target, giver)

    def On_Application(self):
        pass

    def On_Start_of_turn(self):
        pass

    def On_Attack(self):
        pass

    def On_End_of_turn(self):
        pass

    def On_Expire(self):
        pass

    def On_Death(self):
        pass

    def On_Move(self):
        pass