from abc import ABC,abstractmethod

class ConditionBase(ABC):
    def __init__(self,duration:int,target:str,giver:str) -> None:
        """
        Duration is the amount of turns before the effect fades.
        Tracks who the status effect is attached to and was given by using the creature id
        """
        super().__init__()
        self.duration = duration
        self.target = target
        self.giver = giver
        self.active = True

    def decDuration(self):
        self.duration -= 1
        if self.duration == 0:
            self.active = False

    @abstractmethod
    def on_turn_start(self):
        pass

    @abstractmethod
    def on_turn_end(self):
        pass

    @abstractmethod
    def before_attack_roll(self):
        pass

    @abstractmethod
    def after_attack_roll(self):
        pass

    @abstractmethod
    def before_damage(self):
        pass

    @abstractmethod
    def after_damage(self):
        pass

    @abstractmethod
    def before_being_attacked_rolls(self):
        pass

    @abstractmethod
    def after_being_attacked_rolls(self):
        pass

    @abstractmethod
    def before_taking_damage(self):
        pass

    @abstractmethod
    def after_taking_damage(self):
        pass

    @abstractmethod
    def before_spell_cast(self):
        pass

    @abstractmethod
    def after_spell_cast(self):
        pass

    @abstractmethod
    def on_short_rest(self):
        pass

    @abstractmethod
    def on_long_rest(self):
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} given to {self.target} by {self.giver} for {self.duration} turns."