import random

class CoffeeMachine:
    def __init__(self):
        self.servings = 0

    def repair(self):
        self.servings = 0

    def serve(self, beverage):
        if self.servings >= 10:
            raise BrokenMachineException()
        self.servings += 1

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."

if __name__ == '__main__':
    mac = CoffeeMachine()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    mac.serve()
    try:
        mac.serve()
    except:
        mac.serve()
    mac.repair()
    mac.serve()