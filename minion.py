class Minion(object):
    def __init__(name,owner):
        self.health = 100
        self.name = name
        self.owner = owner
    def update (self,*args):
        if args[0]=="hit":
            pass
