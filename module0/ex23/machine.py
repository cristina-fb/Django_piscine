import random
from beverages import *

class CoffeeMachine:
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.servings = 0

    def repair(self):
        self.servings = 0

    def serve(self, beverage):
        if self.servings >= 10:
            raise self.BrokenMachineException()
        self.servings += 1
        if random.randint(0, 5) == 0:
            return EmptyCup()
        else:
            if beverage == 'Coffee':
                return Coffee()
            elif beverage == 'Tea':
                return Tea()
            elif beverage == 'Chocolate':
                return Chocolate()
            elif beverage == 'Capuccino':
                return Capuccino()
            else:
                return EmptyCup()

if __name__ == '__main__':
    mac = CoffeeMachine()
    print(mac.serve('Tea'))
    print()
    print(mac.serve('Chocolate'))
    print()
    print(mac.serve('Capuccino'))
    print()
    print(mac.serve('Coffee'))
    print()
    print(mac.serve('Water'))
    print()
    print( mac.serve('Tea'))
    print()
    print(mac.serve('Chocolate'))
    print()
    print(mac.serve('Capuccino'))
    print()
    print(mac.serve('Coffee'))
    print()
    print(mac.serve('Coffe'))
    print()
    try:
        print(mac.serve('Chocolate'))
    except Exception as ex:
        print(ex)
        print()
    try:
        print(mac.serve('Tea'))
    except Exception as ex:
        print(ex)
        print()
    mac.repair()
    print(mac.serve('Capuccino'))