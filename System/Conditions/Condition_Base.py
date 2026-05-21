from abc import ABC,abstractmethod

class Condition(ABC):
    def __init__(self,duration:int,target:str,giver:str) -> None:
        """
        Duration is the amount of turns before the effect fades.
        Tracks who the status effect is attached to and was given by using the creature id
        """
        super().__init__()
        self.duration = duration
        self.target = target
        self.giver = giver

    @abstractmethod
    def On_Application(self):
        pass

    @abstractmethod
    def On_Start_of_turn(self):
        pass

    @abstractmethod
    def On_Attack(self):
        pass

    @abstractmethod
    def On_End_of_turn(self):
        pass

    @abstractmethod
    def On_Expire(self):
        pass

    @abstractmethod
    def On_Death(self):
        pass

    @abstractmethod
    def On_Move(self):
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} given to {self.target} by {self.giver} for {self.duration} turns."