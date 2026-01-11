from abc import ABC, abstractmethod
from behaviors import WeaponBehavior, SwordBehavior, BowAndArrowBehavior, KnifeBehavior, AxeBehavior


class Character(ABC):
    weapon_behavior: WeaponBehavior

    def set_weapon_behavior(self, wb: WeaponBehavior):
        self.weapon_behavior = wb

    @abstractmethod
    def fight(self):
        ...


class Knight(Character):
    def __init__(self):
        self.weapon_behavior = SwordBehavior()
    
    def fight(self):
        self.weapon_behavior.use_weapon()


class Queen(Character):
    def __init__(self):
        self.weapon_behavior = BowAndArrowBehavior()

    def fight(self):
        self.weapon_behavior.use_weapon()


class King(Character):
    def __init__(self):
        self.weapon_behavior = AxeBehavior()

    def fight(self):
        self.weapon_behavior.use_weapon()
