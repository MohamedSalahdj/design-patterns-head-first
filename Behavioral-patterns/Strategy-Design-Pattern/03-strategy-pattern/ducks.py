from abc import ABC, abstractmethod

from behaviors import FlyBehavior, QuackBehavior, FlyWithWings, Quack, FlyNoWay, Squeak


class Duck(ABC):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    @abstractmethod
    def display(self):
        ...
    
    def perform_fly(self):
        self.fly_behavior.fly()
    
    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a Mallard duck!")


class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a rubber duck!")