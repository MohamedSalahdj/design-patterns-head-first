from behaviors import QuackBehavior, Quack, Squeak, MuteQuack


class DuckCall:
    def __init__(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    def perform_quack(self):
        self.quack_behavior.quack()


if __name__ == "__main__":
    duck_call = DuckCall(Quack())
    duck_call.perform_quack()
    print("Changing quack behavior to Squeak")
    duck_call.set_quack_behavior(Squeak())
    duck_call.perform_quack()
