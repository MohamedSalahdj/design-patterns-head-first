from abc import ABC, abstractmethod

class Quackable(ABC):
    @abstractmethod
    def quack(self):
        ...


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        ...


class Duck:
    def swim(self):
        print("Swims in the pond.")

    def display(self):
        raise NotImplementedError("Subclasses must implement display method.")


class MallardDuck(Duck, Flyable, Quackable):
    def fly(self):
        print("Flies in the sky.")

    def display(self):
        print("I'm a Mallard Duck")


class RedHeadDuck(Duck, Flyable, Quackable):
    def display(self):
        print("I'm a Red Head Duck.")

    def fly(self):
        print("Flies in the sky.")

    def quack(self):
        print("Quack!")


class RubberDuck(Duck, Quackable):
    def display(self):
        print("I'm a Rubber Duck.")

    def quack(self):
        print("Squeak!")


class DecoyWoodDuck(Duck):
    def display(self):
        print("I'm a Decoy Wood Duck.")