class Pokemon:
    def __init__(self, name=""):
        self.__name = name
        self.__types = []
        self.__attack = None
        self.__defense = None
        self.__hp = None
        self.__level = 1
        self.__xp = 0
        self.__id = ""
        self.__in_use = False

    def load_from_POKEMON_DATA_dict(self, dict):
        self.set_name(dict["name"])
        self.set_types(dict["type"])
        self.set_attack(dict["attack"])
        self.set_defense(dict["defense"])
        self.set_hp(dict["hp"])

    def is_alive(self):
        if self.get_hp() > 0:
            return True
        return False

    def attack(self, enemy, hp):
        enemy.set_hp(enemy.get_hp() - hp)

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

    def get_id(self):
        return self.__id
    
    def get_in_use(self):
        return self.__in_use
    
    def set_name(self, name):
        self.__name = name
    
    def set_types(self, types):
        self.__types = types

    def set_attack(self, attack):
        self.__attack = attack
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def set_hp(self, hp):
        if hp is None:
            self.__hp = 0
            return
        try:
            hp = float(hp)
        except:
            hp = 0
        if hp < 0:
            hp = 0
        self.__hp = hp

    def set_level(self, level):
        self.__level = level
    
    def set_xp(self, xp):
        self.__xp = xp
    
    def set_id(self, str_id):
        self.__id = str_id
    
    def set_in_use(self, in_use):
        self.__in_use = in_use

    def add_xp(self, xp):
        self.__xp += xp

    def add_level(self):
        self.__level += 1

    def xp_needed_for_next_level(self):
        return 50 + (self.__level - 1) * 25

    def gain_xp_and_level_up(self, xp_amount):
        self.__xp += xp_amount
        leveled = False

        while self.__xp >= self.xp_needed_for_next_level():
            self.__xp -= self.xp_needed_for_next_level()
            self.__level += 1
            self.__attack += 2
            self.__defense += 1
            self.set_hp(self.__hp + 5)
            leveled = True

        return leveled