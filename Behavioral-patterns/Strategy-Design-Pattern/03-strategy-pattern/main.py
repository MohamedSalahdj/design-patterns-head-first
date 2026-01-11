from ducks import MallardDuck, RubberDuck, ModelDuck

from behaviors import FlyRocketPowered


if __name__ == "__main__":

    d = [MallardDuck(), RubberDuck()]

    for duck in d:
        duck.display()
        duck.perform_fly()
        duck.perform_quack()
        duck.swim()
        print("--"*15)

    # Change the behavior in runtime
    model_duck = ModelDuck()
    model_duck.perform_fly()
    print("##"*15)

    model_duck.set_fly_behavior(FlyRocketPowered())
    model_duck.perform_fly()