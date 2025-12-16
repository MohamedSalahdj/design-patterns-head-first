class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swims in the pond.")

    def fly(self):
        print("Flies in the sky.")

    def display(self):
        raise NotImplementedError("Subclasses must implement display method.")


class MallardDuck(Duck):
    def display(self):
        print("I'm a Mallard Duck")


class RedHeadDduck(Duck):
    def display(self):
        print("I'm a Red Head Duck.")


class RubberDuck(Duck):
    def display(self):
        print("I'm a Rubber Duck.")

    def fly(self):
        print("I can't fly.")


class DecoyWoodDuck(Duck):
    def display(self):
        print("I'm a Decoy Wood Duck.")

    def quack(self):
        print("I can't quack.")

    def fly(self):
        print("I can't fly.")