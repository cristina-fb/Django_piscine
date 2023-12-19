class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return "name : " + self.name + "\nprice : " + str(self.price) + "\ndecription : " + self.description()

class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self)
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Capuccino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "capuccino"
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

class EmptyCup(HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"
        
        def description(self):
            return "An empty cup?! Gimme my money back!"