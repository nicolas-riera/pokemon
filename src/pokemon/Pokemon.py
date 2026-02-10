class Pokemon:
    def __init__(self, name:str):
        self.name = name
        self.types = []
        self.attack = None
        self.defense = None
        self.hp = None
    
    def load(self, file):
        pass