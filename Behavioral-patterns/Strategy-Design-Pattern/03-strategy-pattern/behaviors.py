from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        ...


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        ...


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with wings!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly.")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")