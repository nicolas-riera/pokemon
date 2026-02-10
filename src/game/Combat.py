from src.assets_loading import POKEMONS_TYPE_STATS
from src.pokemon.Pokemon import Pokemon

class Combat:
    def __init__(self):
        pass

    def calculate_attack_mult(self, attack_type:str, enemy:object):
        mult = 1
        
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type][def_type]
        return mult
            

