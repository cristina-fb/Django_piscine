class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
            self.name = name
    
    def __str__(self):
        return self.name
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    anon = Intern()
    mark = Intern('Mark')
    print(anon)
    print(mark)
    coffee = mark.make_coffee()
    print(coffee)
    try:
        anon.work()
    except Exception as ex:
        print(ex)