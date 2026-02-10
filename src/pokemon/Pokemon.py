class Pokemon:
    def __init__(self, name:str):
        self.name = name
        self.types = []
        self.attack = None
        self.defense = None
        self.hp = None
    
    def load(self, file):
        pass

    def __repr__(self): #special method for debbugin purpose return our pokemon list as a string and format that list
        return f"{{'name': '{self.name}', 'types': {self.types}, 'attack': {self.attack}, 'defense': {self.defense}, 'hp': {self.hp}}}"