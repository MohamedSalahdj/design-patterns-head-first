class Quackable:
    def quack(self):
        print("Quack!")


class Flyable:
    def fly(self):
        print("Flies in the sky.")


class Duck:
    def swim(self):
        print("Swims in the pond.")

    def display(self):
        ...


class MallardDuck(Duck, Flyable, Quackable):
    def display(self):
        print("I'm a Mallard Duck")


class RedHeadDduck(Duck, Flyable, Quackable):
    def display(self):
        print("I'm a Red Head Duck.")


class RubberDuck(Duck, Quackable):
    def display(self):
        print("I'm a Rubber Duck.")


class DecoyWoodDuck(Duck):
    def display(self):
        print("I'm a Decoy Wood Duck.")