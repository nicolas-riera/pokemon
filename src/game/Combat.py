from src.assets_loading import POKEMONS_TYPE_STATS, POKEMON_DATA
from src.pokemon.Pokemon import Pokemon

import random

class Combat:
    def __init__(self):
        self.first_run = True
        self.ally = None
        self.turn_of_ally = True
        self.enemy = None
        self.state = "game"

    @staticmethod
    def __calculate_attack_mult(attack_type:str, enemy:object):
        mult = 1
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type][def_type]

        return mult
    
    @staticmethod
    def __select_random_pokemon_from_POKEMON_DATA(ally):
        pokemon = Pokemon()

        random_pokemon_dict = random.choice(list(POKEMON_DATA.values()))
        pokemon.load_from_POKEMON_DATA_dict(random_pokemon_dict)
        pokemon.set_level(random.randint(
            ally.get_level() - 1, ally.get_level() + 1)
        )

        return pokemon

    def __attack(self, src, dest):
        dest.receive_attack(src.get_attack())

    def events(self):
        pass

    def draw(self):
        pass

    def logic(self, ally):
        if self.first_run:
            self.turn_of_ally = True
            self.first_run = False
            self.enemy = self.__select_random_pokemon_from_POKEMON_DATA(ally)

        if self.state == "game" and len(ally.get_types()) == 1:
            self.__attack(ally, self.enemy)


        # if self.state == "pre_attack":
        #     if self.turn_of_ally:
        #         self.__attack(self.ally, self.enemy)
        #     else:
        #         self.__attack(self.enemy, self.enemy)


        return self.state