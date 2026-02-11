class Pokemon:
    def __init__(self, name:str):
        self.__name = name
        self.__types = []
        self.__attack = None
        self.__defense = None
        self.__hp = None
        self.__level = 1
        self.__xp = 0

    def get_name(self):
        return self.__name

    def get_types(self):
        return self.__types
    
    def get_attack(self):
        return self.__attack
    
    def get_defense(self):
        return self.__defense
    
    def get_hp(self):
        return self.__hp
    
    def get_level(self):
        return self.__level
    
    def get_xp(self):
        return self.__xp
    
    def set_name(self, name):
        self.__name = name
    
    def set_types(self, types):
        self.__types = types

    def set_attack(self, attack):
        self.__attack = attack
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def set_hp(self, hp):
        self.__hp = hp

    def set_level(self, level):
        self.__level = level
    
    def set_xp(self, xp):
        self.__xp = xp