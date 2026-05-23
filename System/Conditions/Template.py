from System.Conditions.Condition_Base import ConditionBase

"""
Copy this file and use as a template for creating new Condition classes.
This file is not made for in game use.
"""

class Template(ConditionBase):
    def __init__(self, duration: int, target: str, giver: str) -> None:
        super().__init__(duration, target, giver)

    def on_turn_start(self):
        pass

    def on_turn_end(self):
        pass

    def before_attack_roll(self):
        pass

    def after_attack_roll(self):
        pass

    def before_damage(self):
        pass

    def after_damage(self):
        pass

    def before_being_attacked_rolls(self):
        pass

    def after_being_attacked_rolls(self):
        pass

    def before_taking_damage(self):
        pass

    def after_taking_damage(self):
        pass

    def before_spell_cast(self):
        pass

    def after_spell_cast(self):
        pass

    def on_short_rest(self):
        pass

    def on_long_rest(self):
        pass