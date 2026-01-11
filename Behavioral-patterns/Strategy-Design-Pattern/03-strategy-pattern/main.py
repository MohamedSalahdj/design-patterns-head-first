from ducks import MallardDuck, RubberDuck


if __name__ == "__main__":

    d = [MallardDuck(), RubberDuck()]
    
    for duck in d: 
        duck.display()
        duck.perform_fly()
        duck.perform_quack()
        duck.swim()
        print("--"*15)