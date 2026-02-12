from src.assets_loading import POKEMONS_TYPE_STATS, POKEMON_DATA
from src.pokemon.Pokemon import Pokemon

import random

class Combat:
    def __init__(self):
        self.first_run = True
        self.ally = None
        self.enemy = None
        self.state = "game"

    def calculate_attack_mult(self, attack_type:str, enemy:object):
        mult = 1
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type][def_type]
        return mult
    
    @staticmethod
    def __select_random_pokemon():
        pokemon = Pokemon()
        # print(POKEMON_DATA)
        random_pokemon = random.choice(list(POKEMON_DATA.values()))
        print(random_pokemon)
        
        return pokemon

    def draw(self):
        pass

    def logic(self, ally):
        if self.first_run:
            self.first_run = False
            self.enemy = self.__select_random_pokemon()

        return self.state 