from abc import ABC, abstractmethod


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        ...


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Cutting with a knife!")


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Shooting an arrow with a bow!")


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Chopping with an axe!")


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Swinging a sword!")